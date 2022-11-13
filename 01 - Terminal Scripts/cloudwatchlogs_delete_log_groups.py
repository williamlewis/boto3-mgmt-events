# Find and delete log groups from CloudWatchLogs

# create boto3 cloudwatchlogs client (NOT the same as cloudwatch client for alarms)
import boto3
client = boto3.client('logs')

# describe log groups to store in a list
groups = client.describe_log_groups()
group_names = []
for group in groups['logGroups']:
    log_group_name = group['logGroupName']
    group_names.append(log_group_name)

# delete group and print a confirmation statement
for name in group_names:
    client.delete_log_group(
        logGroupName=name
    )
    print(f'Log Group "{name}" has been successfully deleted.')
