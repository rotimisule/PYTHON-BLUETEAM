import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Describe instances that are running and have the tag 'Environment: Dev'
response = ec2.describe_instances(
    Filters=[
        {'Name': 'instance-state-name', 'Values': ['running']},
        {'Name': 'tag:Enviornment', 'Values': ['Dev']}
    ]
)

# Extract instance IDs from the response
instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

# Check if there are instances to stop
if instances:
    # Stop the identified instances
    ec2.stop_instances(InstanceIds=instances)
    # Print the list of stopped instance IDs
    print("Stopped the following Dev instances:", *instances)
else:
    # If no instances found, print a message
    print("No running Dev instances found.")
