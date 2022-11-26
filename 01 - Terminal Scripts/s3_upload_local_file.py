# Upload a local file to an S3 bucket

# create boto3 S3 resource
import boto3
s3 = boto3.resource('s3')

# specify destination bucket, file path, & file name
bucket_name = 'demo-csv-upload'
file_path = 'C:\\Users\\wille\Desktop\\employees.csv'
file_name = 'employees.csv'

# upload file; use the META.CLIENT to access client methods through the resource (e.g. when the resource doesn't support an operation and you've already written code around the resource) 
s3.meta.client.upload_file(file_path, bucket_name, file_name)

# print success statement to indicate end of script
print(f'File {file_name} was successfully uploaded into bucket {bucket_name}')
