# Find and delete all S3 buckets, including objects and object versions

# create boto3 S3 resource
import boto3
s3 = boto3.resource('s3')

# print list of all current buckets
buckets = list(s3.buckets.all())
print('----  BUCKET SUMMARY BEFORE DELETION  ----')
for bucket in s3.buckets.all():
    print(str(bucket.creation_date)[:10] + '    ----    ' + bucket.name)

# delete object versions, objects, & buckets
for bucket in buckets:
    try:
        bucket.object_versions.delete()
        print('Deleting object versions...')
    except:
        print('No object versions found')
    bucket.delete()
    print('Deleting ' + bucket.name + ' ...')

# print statement to indicate end of script
print('All S3 buckets have been successfully deleted.')
