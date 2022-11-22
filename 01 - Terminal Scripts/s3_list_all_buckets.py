# List all current S3 buckets

# create boto3 S3 client
import boto3
client = boto3.client('s3')

# list buckets & print names from response
response = client.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])
