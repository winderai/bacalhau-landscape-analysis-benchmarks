# Launch AWS Infrastructure 

## Prerequistes

* [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) (tested on `v2.4.17`)
* Enough EC2 quota to launch multiple instances
* EC2 permissions to set up a security group
* [EC2 key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html), we'll store its name in `KEY_NAME`

## Setup some env vars:

```bash
# aws cli
export AWS_PROFILE=winder
export AWS_REGION=eu-central-1
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

# this exposes the security group to any inbound traffic for the Internet
# make sure to terminate the EC2 instances once the benchmark has completed
aws ec2 authorize-security-group-ingress \
    --group-name $PROJ_NAME \
    --protocol all \
    --port 0-65535 \
    --cidr 0.0.0.0/0 \
    --tag-specifications "ResourceType=security-group-rule,Tags=[{Key=project,Value=$PROJ_NAME},{Key=Name,Value=$PROJ_NAME}]"
```

## Launch EC2 instances

Configure the cluster resources, set `EC2_COUNT` to 1 for running the benchmarks in a single node setting.

```bash
export EC2_COUNT=1
export EC2_INSTANCE_TYPE=t2.large
export AMI_ID=ami-0d527b8c289b4af7f
export EBS_SIZE=75
export KEY_NAME=wr-enrico-aws-ec2
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

Retrieve public IPs:

```bash
aws ec2 describe-instances \
    --filters "Name=tag-value,Values=$PROJ_NAME" \
    --query "Reservations[*].Instances[*].PublicIpAddress" \
    --output text
```

## Cleanup EC2

```bash
aws ec2 terminate-instances --instance-ids $(aws ec2 describe-instances \
        --query 'Reservations[].Instances[].InstanceId' \
        --filters "Name=tag:Name,Values=$PROJ_NAME" \
        --output text\
)
```
