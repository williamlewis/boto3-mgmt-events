# List all objects in a specific S3 bucket

# create boto3 S3 client & define bucket
import boto3
client = boto3.client('s3')

# list objects & print object key(s)
bucket_name = '' # update bucket name here

response = client.list_objects(
    Bucket=bucket_name
)

for object in response['Contents']:
    print(object['Key'])

# indicate end of script
print('Script complete.')
