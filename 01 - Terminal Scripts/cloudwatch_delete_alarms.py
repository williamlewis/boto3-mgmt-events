# Delete CloudWatch metric alarms

# create boto3 resource for CloudWatch (NOT CloudWatchLogs)
import boto3
cloudwatch = boto3.resource('cloudwatch')

# use collection to get all alarms
alarms = cloudwatch.alarms.all()

# use Alarm class to delete those found
for alarm in alarms:
    alarm.delete()
    print(f'{alarm.name} has been deleted.')

# check number of alarms remaining & print number to indicate end of script
remaining_alarms = cloudwatch.alarms.all()
num_remaining_alarms = len(list(remaining_alarms))
print(f'{num_remaining_alarms} alarms remaining in account.')
