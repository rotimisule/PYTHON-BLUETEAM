import boto3

ec2=boto3.client('ec2')

sg_id='sg-0b285d2deaab69a7e'

response = ec2.authorize_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[
        {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                   
                },
            ],
            'ToPort': 22,
        },
         {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                   
                },
            ],
            'ToPort': 80,
        },
    ],
)

print(response)