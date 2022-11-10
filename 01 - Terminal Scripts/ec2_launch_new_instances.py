# Launch a specified number of new instances from defined AMI & instance type

# create boto3 ec2 client
import boto3
client = boto3.client('ec2')

# launch instances by providing AMI image id, instance type, & number
resp = client.run_instances(
    ImageId='ami-026b57f3c383c2eec',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)

# print instance ids to indicate end of script
for instance in resp['Instances']:
    new_inst_id = instance['InstanceId']
    print(f'New instance {new_inst_id} has been launched.')
