# List out InstanceId attribute for all current instances

# create boto3 ec2 resource
import boto3
ec2 = boto3.resource('ec2')

# use resource collection to get all instances
instances = ec2.instances.all()

# print ids to indicate end of script
if len(list(instances)) > 0:
    print('Current EC2 Instances:')
    for instance in instances:
        print(instance.instance_id)
else:
    print('There are currently no EC2 instances.')
