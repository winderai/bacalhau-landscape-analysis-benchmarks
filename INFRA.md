# sample-code-benchmark

# AWS
❯ aws --version
aws-cli/2.4.17 Python/3.8.8 Darwin/20.6.0 exe/x86_64 prompt/off


export AWS_PROFILE=winder
export AWS_REGION=eu-central-1
aws --profile $AWS_PROFILE --region $AWS_REGION ec2 describe-instances


aws ec2 create-security-group \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --group-name ProtocolLabsDEV \
    --description "ProtocolLabs dev security group" \
    --tag-specifications 'ResourceType=security-group,Tags=[{Key=project,Value=ProtocolLabs},{Key=Name,Value=ProtocolLabs-dev}]'

aws ec2 authorize-security-group-ingress \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --group-name ProtocolLabsDEV \
    --protocol all \
    --port 0-65535 \
    --cidr 0.0.0.0/8 \
    --tag-specifications 'ResourceType=security-group-rule,Tags=[{Key=project,Value=ProtocolLabs},{Key=Name,Value=ProtocolLabs-dev}]'

aws ec2 authorize-security-group-ingress \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --group-name ProtocolLabsDEV \
    --protocol tcp \
    --port 0-65535 \
    --cidr 0.0.0.0/0 \
    --tag-specifications 'ResourceType=security-group-rule,Tags=[{Key=project,Value=ProtocolLabs},{Key=Name,Value=ProtocolLabs-dev}]'

aws ec2 run-instances \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --image-id ami-0d527b8c289b4af7f \
    --count 2 \
    --instance-type t2.xlarge \
    --key-name wr-enrico-aws-ec2 \
    --security-group-ids ProtocolLabsDEV \
    --block-device-mapping DeviceName=/dev/sda1,Ebs={VolumeSize=120} \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=project,Value=ProtocolLabs},{Key=Name,Value=ProtocolLabs-dev}]' 'ResourceType=volume,Tags=[{Key=project,Value=ProtocolLabs},{Key=Name,Value=ProtocolLabs-dev}]'


aws ec2 describe-instances \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --filters "Name=tag-value,Values=ProtocolLabs-dev" \
    --query "Reservations[*].Instances[*].PublicIpAddress" \
    --output text


ssh -i "~/.ssh/wr-enrico-aws-ec2.pem" ubuntu@3.71.202.247
ssh -i "~/.ssh/wr-enrico-aws-ec2.pem" ubuntu@3.66.120.241


# Cleanup EC2

aws ec2 terminate-instances --profile $AWS_PROFILE --region $AWS_REGION --instance-ids $(aws ec2 describe-instances --profile $AWS_PROFILE --region $AWS_REGION --query 'Reservations[].Instances[].InstanceId' --filters "Name=tag:Name,Values=ProtocolLabs-dev" --output text)