# Delete CloudWatch metric alarms

# create boto3 resource for CloudWatch (NOT CloudWatchLogs)
# use collection to get all alarms
# use Alarm class to delete those found
# print alarm name for those deleted to indicate end of script
