# Launch AWS Infrastructure 

## Prerequistes

* [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) (tested on `v2.4.17`)
* Enough EC2 quota to launch multiple instances
* EC2 permissions to set up a security group
* [EC2 key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html), we'll store its name in `KEY_NAME`

## Setup some env vars:

```bash
# aws cli
export AWS_PROFILE=<your-aws-profile>
export AWS_REGION=<your-aws-region>
# ec2
export PROJ_NAME=ProtocolLabsDEV
export GROUP_NAME_DESCRIPT="ProtocolLabs dev security group"
```

## Configure security group


```bash
aws ec2 create-security-group \
    --group-name $PROJ_NAME \
    --description $GROUP_NAME_DESCRIPT \
    --tag-specifications "ResourceType=security-group,Tags=[{Key=project,Value=$PROJ_NAME},{Key=Name,Value=$PROJ_NAME}]"
```

Create an ad-hoc ingress rule, for security reasons we restrict inbout traffic from a single IP address.
Please set `YOUR_IP_ADDRESS` accordingly; this is the IP of your workstation, try querying https://www.myip.com/ or contact your system admin or ISP to find your exact address.

```bash
aws ec2 authorize-security-group-ingress \
    --group-name $PROJ_NAME \
    --protocol all \
    --port 0-65535 \
    --cidr $YOUR_IP_ADDRESS/32 \
    --tag-specifications "ResourceType=security-group-rule,Tags=[{Key=project,Value=$PROJ_NAME},{Key=Name,Value=$PROJ_NAME}]"
```

Allow traffic from private IP range `172.16.0.0 – 172.31.255.255`.
You may need to use a different CIDR if your EC2 hosts fall within a different IP range.

```bash
aws ec2 authorize-security-group-ingress \
    --group-name $PROJ_NAME \
    --protocol all \
    --port 0-65535 \
    --cidr 172.16.0.0/12 \
    --tag-specifications "ResourceType=security-group-rule,Tags=[{Key=project,Value=$PROJ_NAME},{Key=Name,Value=$PROJ_NAME}]"
```

## Launch EC2 instances

Configure the cluster resources, note each machine we launch here will have the same resources.
To run the benchmarks in a single node setting set `EC2_COUNT` to 1.
For the purpose of benchmarking performance, it's important to use instance type with a consistent workload capacity, therefore, we recommend using M5 instances.


```bash
export EC2_COUNT=<set-nr-of-hosts>
export EC2_INSTANCE_TYPE=<pick-an-ec2-instance-type>
export AMI_ID=ami-0d527b8c289b4af7f # Important! Make sure you use this AMI!
export EBS_SIZE=75 # This disk size is sufficient for running all code samples and benchmarks
export KEY_NAME=<your-key-pair-name>
```

```bash
aws ec2 run-instances \
    --image-id $AMI_ID \
    --count $EC2_COUNT \
    --instance-type $EC2_INSTANCE_TYPE \
    --key-name $KEY_NAME \
    --security-group-ids $PROJ_NAME \
    --block-device-mapping DeviceName=/dev/sda1,Ebs={VolumeSize=$EBS_SIZE} \
    --tag-specifications "ResourceType=instance,Tags=[{Key=project,Value=$PROJ_NAME},{Key=Name,Value=$PROJ_NAME}]" "ResourceType=volume,Tags=[{Key=project,Value=$PROJ_NAME},{Key=Name,Value=$PROJ_NAME}]"
```

Retrieve public IPs either via EC2 console or the following command:

```bash
aws ec2 describe-instances \
    --filters "Name=tag-value,Values=$PROJ_NAME" \
    --query "Reservations[*].Instances[*].PublicIpAddress" \
    --output text
```

---

## Cleanup EC2 (only when your're done with the benchmarks)

```bash
aws ec2 terminate-instances --instance-ids $(aws ec2 describe-instances \
        --query 'Reservations[].Instances[].InstanceId' \
        --filters "Name=tag:Name,Values=$PROJ_NAME" \
        --output text\
)
```

You may need to manually delete the security group as well.
