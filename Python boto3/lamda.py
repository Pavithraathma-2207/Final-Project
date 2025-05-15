import boto3
import json

# Initialize the AWS Lambda client
lambda_client = boto3.client('lambda')


function_name = 'MyHelloLambda'

# Payload data to send to the Lambda function
payload = {
    "key1": "value1",
    "key2": "value2"
}

# Invoke the Lambda function synchronously
response = lambda_client.invoke(
    FunctionName=function_name,
    InvocationType='RequestResponse',
    Payload=json.dumps(payload),
)

# Read the response
response_payload = json.load(response['Payload'])

# Print the Lambda response
print("Lambda response:")
print(json.dumps(response_payload, indent=2))
