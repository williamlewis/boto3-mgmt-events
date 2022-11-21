# Terminate all current EC2 instances

# create boto3 EC2 resource & get all instances with collection
import boto3
ec2 = boto3.resource('ec2')

instances = ec2.instances.all()

# terminate instances & print statement to indicate end of script
for instance in instances:
    instance.terminate()
    print(f'Instance with Id = {instance.instance_id} has been successfully terminated.')
