# Delete a specific Lambda function

# create boto3 client
import boto3
client = boto3.client('lambda')

# delete function by function name
function_name = 'csv_s3_dynamodb' # sample value used
client.delete_function(
    FunctionName=function_name
)

# print msg to indicate end of script
print(f'Function {function_name} has been successfully deleted.')
