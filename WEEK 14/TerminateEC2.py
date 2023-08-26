import boto3
ec2 = boto3.client('ec2')

response = ec2.terminate_instances(
    InstanceIds=[
        'i-0be39624d344c113a','i-0c90dc9c72d5ffe88','i-0ce5c3ed7135fae92'
    ],
)
print("The instances have been terminated ")