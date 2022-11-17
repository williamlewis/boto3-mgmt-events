# Delete a table in DynamoDB

# create boto3 DynamoDB resource & get table by name
import boto3
dyn = boto3.resource('dynamodb')

table_name = 'employees-batch-demo'
table = dyn.Table(table_name)

# delete table & get status
response = table.delete()
table_state = response['TableDescription']['TableStatus']

# print statement to indicate end of script
print(f'Table "{table_name}" has been successfully deleted; table status is now "{table_state}".')
