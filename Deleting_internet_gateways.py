import boto3

ec2 = boto3.client('ec2')

delete = ec2.delete_internet_gateway(
    InternetGatewayId='igw-01125b687b468248a'
)

