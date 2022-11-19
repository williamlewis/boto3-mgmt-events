# Delete instance snapshots created by self

# create boto3 EC2 resource & get self-owned snapshots with collection
import boto3
ec2 = boto3.resource('ec2')

snapshots = ec2.snapshots.filter(OwnerIds=['self'])

# delete snapshots & print confirmation statement
for snapshot in snapshots:
    snapshot.delete()
    print(f'Snapshot with Id = {snapshot.snapshot_id} is deleted')
