export AWS_PROFILE=winder
export AWS_DEFAULT_REGION=eu-central-1


# install aws cli first and configure it with credentials and default region
# the script will iterate over all regions of AWS

for region in `aws ec2 describe-regions --output text | cut -f4`
do
     echo -e "\nListing Instances in region:'$region'..."
     aws ec2 describe-instances --query "Reservations[*].Instances[*].{IP:PublicIpAddress,ID:InstanceId,Type:InstanceType,State:State.Name,Name:Tags[0].Value}" --output=table --region $region
done