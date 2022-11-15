# Create a new S3 bucket

# set up boto3 S3 resource
import boto3
s3_resource = boto3.resource('s3')

# provide bucket name & create bucket
bucket_name = 'demo-csv-upload'

s3_resource.create_bucket(
    Bucket=bucket_name
)

# print confirmation to indicate end of script
print(f'Bucket "{bucket_name}" was successfully created.')
