# Delete a specific S3 bucket including all objects and object versions within

# create boto3 S3 resource, get bucket & objects collection
import boto3
s3 = boto3.resource('s3')

bucket_name = 'demo-csv-upload' # update bucket name to run
bucket = s3.Bucket(bucket_name)

objects = bucket.objects.all()


# loop over objects to delete versions, then objects, then overall bucket
for object in objects:
    obj_key = object.key
    obj_bucket = object.bucket_name
    try:
        object.object_versions.delete()
        print(f'Deleting object VERSIONS of object "{object.key}"')
    except:
        print('*Couldn\'t delete object versions*')
    
    try:
        object.delete()
        print(f'Deleting OBJECT "{object.key}" from bucket "{obj_bucket}"')
    except:
        print('*Couldn\'t delete object*')
    
    try:
        bucket.delete()
        print(f'Deleting BUCKET "{bucket_name}"')
    except:
        print('*Couldn\'t delete bucket*')


# print statement to confirm script is complete
print('Script complete.')
