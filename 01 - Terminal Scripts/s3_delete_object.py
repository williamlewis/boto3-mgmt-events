# Delete a single object from an S3 bucket

# set up boto3 S3 client & define bucket / object inputs
import boto3
client = boto3.client('s3')

bucket_name = '' # update with bucket name
key_name = '' # update with object name, including file type extension

# delete named object from named bucket
response = client.delete_object(
    Bucket=bucket_name,
    Key=key_name
)

# print statement to indicate end of script
print(f'{key_name} has been deleted from {bucket_name} bucket.')
