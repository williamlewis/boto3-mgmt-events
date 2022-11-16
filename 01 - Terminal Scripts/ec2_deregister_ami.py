# Deregister (delete) a custom machine image from a specific region

# create boto3 EC2 resource for one region (AMIs live within EC2 service)
import boto3

aws_region = 'us-east-1'

ec2_resource = boto3.resource('ec2', region_name=aws_region)
ami_id = 'ami-03891ebcf1bd3cbb5'

# deregister AMI
image = ec2_resource.Image(ami_id)
image.deregister()

# print confirmation statement to indicate end of script
print(f'AMI with Id {ami_id} has successfully been deregistered.')
