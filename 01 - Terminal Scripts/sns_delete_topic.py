# Delete an SNS topic and related subscriptions

# create boto3 client
import boto3
sns = boto3.client('sns')

# delete topic and indicate end of script
sns.delete_topic(
    TopicArn='arn:aws:sns:us-east-1:095304811476:snapshots' # update input here
)
print('SNS topic has been deleted.')
