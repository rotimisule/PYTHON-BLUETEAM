import boto3

ec2=boto3.client('ec2')

response =ec2.create_security_group(
    Description="Security group from boto3",
    GroupName='GLOTIMI-SG',
    VpcId='vpc-042c27a5f243b3ddd',
)

print(response["GroupId"])
