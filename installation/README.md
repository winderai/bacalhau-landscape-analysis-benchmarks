# Raise AWS Infrastructure 

## Prerequistes

* AWS cli (aws-cli/2.4.17)
* enough EC2 quota


## 1) Let's setup some env vars:

```
export AWS_PROFILE=winder
export AWS_REGION=eu-central-1
export PROJ_NAME=ProtocolLabsDEV
export GROUP_NAME_DESCRIPT="ProtocolLabs dev security group"
export AMI_ID=ami-0d527b8c289b4af7f
export EC2_COUNT=1
export EC2_INSTANCE_TYPE=t2.micro
export KEY_NAME=wr-enrico-aws-ec2
export EBS_SIZE=25
```

## 2) Configure security group


```
aws ec2 create-security-group \
    --group-name $PROJ_NAME \
    --description $GROUP_NAME_DESCRIPT \
    --tag-specifications "ResourceType=security-group,Tags=[{Key=project,Value=$PROJ_NAME},{Key=Name,Value=$PROJ_NAME}]"

aws ec2 authorize-security-group-ingress \
    --group-name $PROJ_NAME \
    --protocol all \
    --port 0-65535 \
    --cidr 0.0.0.0/0 \
    --tag-specifications "ResourceType=security-group-rule,Tags=[{Key=project,Value=$PROJ_NAME},{Key=Name,Value=$PROJ_NAME}]"
```

## 3) Launch EC2 instances

```
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

```
aws ec2 describe-instances \
    --filters "Name=tag-value,Values=$PROJ_NAME" \
    --query "Reservations[*].Instances[*].PublicIpAddress" \
    --output text
```

# Cleanup EC2

```
aws ec2 terminate-instances --instance-ids $(aws ec2 describe-instances \
        --query 'Reservations[].Instances[].InstanceId' \
        --filters "Name=tag:Name,Values=$PROJ_NAME" \
        --output text\
)
```