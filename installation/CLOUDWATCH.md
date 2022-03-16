# Collecting metrics from Amazon EC2 instances with the CloudWatch agent

These instructions allow you to collect a variety of performance metrics from you cluster nodes, sampled every 60 seconds, including:

- cpu usage
- memory usage
- disk usage
- network usage

Note: metrics collected by the CloudWatch agent are billed as custom metrics.


# Prerequistes

The target OS is Ubuntu (x86_64), you'll need `aws-cli` installed.

### Create an IAM role to use with the CloudWatch agent on Amazon EC2 instances

Follow the 12-step guide on AWS docs from the ["To create the IAM role necessary for each server to run the CloudWatch agent"](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent.html#create-iam-roles-for-cloudwatch-agent-roles) paragraph.
You won't be using Systems Manager so ignore the `AmazonSSMManagedInstanceCore` policy, instead use `CloudWatchAgentServerPolicy` only.


### Assign IAM role to instances

Open the IAM console at https://console.aws.amazon.com/iam/ and find the `Instance profile ARN` of the Role created in the step above (example: `arn:aws:iam::xxxxxxxxxx:instance-profile/ProtocolLabs-CloudWatchAgentServerRole`).
Save it in `export AWS_INSTANCE_PROFILE_ARN="<your-instance-profile-arn>"`.

Now run the following command for each EC2 instance in your cluster.
Replace `<your-ec2-instance-ID>` with the right `Instance ID`, you can find that value either in the AWS console or by running `ec2metadata --instance-id` from within the host.

```
aws ec2 associate-iam-instance-profile \
    --instance-id "<your-ec2-instance-ID>" \
    --iam-instance-profile Arn=${AWS_INSTANCE_PROFILE_ARN}
```

# Install the CloudWatch agent

Run the following commands on each host, this way you'll be able to fetch metrics from the whole cluster.

## Download and install deb package

Make sure you have the `AWS_REGION` environment variable set up.

```
wget "https://s3.${AWS_REGION}.amazonaws.com/amazoncloudwatch-agent-${AWS_REGION}/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb"
sudo dpkg -i -E ./amazon-cloudwatch-agent.deb
```

## Install collectd

```
sudo apt update
sudo apt install -y collectd
```

## Start the CloudWatch agent

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:amazon-cloudwatch-agent.json
```

<!-- ## Get metrics


aws cloudwatch list-metrics --namespace "CWAgent"


start_time=$(date -v-1d '+%Y-%m-%dT%H:%M:%S')
now=$(date '+%Y-%m-%dT%H:%M:%S')

aws --output json cloudwatch get-metric-statistics --namespace CWAgent \
    --metric-name cpu_usage_system --statistics Average  --period 3600 \
    --start-time $start_time --end-time $now -->