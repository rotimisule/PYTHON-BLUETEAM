import boto3

ec2=boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-0b285d2deaab69a7e',
)

print(response)