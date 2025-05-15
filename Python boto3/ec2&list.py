import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.client('ec2')

# Describe the instances
response = ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
)

# Print information about running instances
print("Running EC2 Instances:")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"Instance Type: {instance['InstanceType']}")
        print(f"Public IP: {instance.get('PublicIpAddress', 'N/A')}")
        print(f"Private IP: {instance['PrivateIpAddress']}")
        print(f"State: {instance['State']['Name']}")
        print("-" * 50)
