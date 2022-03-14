# Collecting metrics from Amazon EC2 instances with the CloudWatch agent

These instructions 
The logs collected by the unified CloudWatch agent are processed and stored in Amazon CloudWatch Logs.
Metrics collected by the CloudWatch agent are billed as custom metrics.

Linux / Ubuntu (x86_64)


## Prerequistes

### Create an IAM role to use with the CloudWatch agent on Amazon EC2 instances

Follow the 12-step guide on AWS docs from the ["To create the IAM role necessary for each server to run the CloudWatch agent"](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent.html#create-iam-roles-for-cloudwatch-agent-roles) paragraph.
You won't be using Systems Manager so ignore the `AmazonSSMManagedInstanceCore` policy, instead use `CloudWatchAgentServerPolicy` only.


## Assign IAM role to instances

```
aws ec2 associate-iam-instance-profile \
    --instance-id "i-09621312a3399db07" \
    --iam-instance-profile Arn="arn:aws:iam::972867294043:instance-profile/ProtocolLabs-CloudWatchAgentServerRole"
```

## Download and configure the CloudWatch agent using the command line

```
export AWS_REGION=eu-central-1

wget "https://s3.${AWS_REGION}.amazonaws.com/amazoncloudwatch-agent-${AWS_REGION}/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb"

sudo dpkg -i -E ./amazon-cloudwatch-agent.deb
```

## Install collectd

```
sudo apt update
sudo apt install -y collectd
```

## Create the CloudWatch agent configuration file

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
```

## Start the CloudWatch agent using the command line

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:amazon-cloudwatch-agent.json
```


## Get metrics


aws cloudwatch list-metrics --namespace "CWAgent"


start_time=$(date -v-1d '+%Y-%m-%dT%H:%M:%S')
now=$(date '+%Y-%m-%dT%H:%M:%S')

aws --output json cloudwatch get-metric-statistics --namespace CWAgent \
    --metric-name cpu_usage_system --statistics Average  --period 3600 \
    --start-time $start_time --end-time $now