# Collecting metrics and logs from Amazon EC2 instances and on-premises servers with the CloudWatch agent

TODO:
- Add Role to AWS instructions
- need to enable advancede monitoring??
- Check if it works

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html

The logs collected by the unified CloudWatch agent are processed and stored in Amazon CloudWatch Logs.
Metrics collected by the CloudWatch agent are billed as custom metrics.

# Linux / Ubutu / x86




## Create IAM roles to use with the CloudWatch agent on Amazon EC2 instances

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent.html#create-iam-roles-for-cloudwatch-agent-roles


12 steps: "To create the IAM role necessary for each server to run the CloudWatch agent"
Ignore `AmazonSSMManagedInstanceCore`


<!-- ## Install AWS cli

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install -y unzip
unzip awscliv2.zip
sudo ./aws/install
```

Configure:

```
mkdir -p ~/.aws

echo "[AmazonCloudWatchAgent]
aws_access_key_id = my_access_key
aws_secret_access_key = my_secret_key
" >> ~/.aws/credentials
```

For `my_access_key` and `my_secret_key`, use the keys from the IAM user that has the permissions to write to Systems Manager Parameter Store. -->

## Download and configure the CloudWatch agent using the command line

```
export AWS_REGION=eu-central-1

wget "https://s3.${AWS_REGION}.amazonaws.com/amazoncloudwatch-agent-${AWS_REGION}/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb"

sudo dpkg -i -E ./amazon-cloudwatch-agent.deb
```

## Create the CloudWatch agent configuration file

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
```

https://github.com/Cloud-Yeti/aws-ec2-course/blob/master/labs/lab08-cloudwatch-agent-and-memory-metric.MD

amazon-cloudwatch-agent.json:

```json
{
	"agent": {
		"metrics_collection_interval": 60,
		"run_as_user": "ubuntu"
	},
	"metrics": {
		"aggregation_dimensions": [
			[
				"InstanceId"
			]
		],
		"metrics_collected": {
			"collectd": {
				"metrics_aggregation_interval": 60
			},
			"cpu": {
				"measurement": [
					"cpu_usage_idle",
					"cpu_usage_iowait",
					"cpu_usage_user",
					"cpu_usage_system"
				],
				"metrics_collection_interval": 60,
				"resources": [
					"*"
				],
				"totalcpu": false
			},
			"disk": {
				"measurement": [
					"used_percent",
					"inodes_free"
				],
				"metrics_collection_interval": 60,
				"resources": [
					"*"
				]
			},
			"diskio": {
				"measurement": [
					"io_time",
					"write_bytes",
					"read_bytes",
					"writes",
					"reads"
				],
				"metrics_collection_interval": 60,
				"resources": [
					"*"
				]
			},
			"mem": {
				"measurement": [
					"mem_used_percent"
				],
				"metrics_collection_interval": 60
			},
			"netstat": {
				"measurement": [
					"tcp_established",
					"tcp_time_wait"
				],
				"metrics_collection_interval": 60
			},
			"swap": {
				"measurement": [
					"swap_used_percent"
				],
				"metrics_collection_interval": 60
			}
		}
	}
}
```


## Install collectd

```
sudo apt update
sudo apt install -y collectd
```

## Start the CloudWatch agent using the command line

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:amazon-cloudwatch-agent.json
```