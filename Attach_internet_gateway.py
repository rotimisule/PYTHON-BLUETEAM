import boto3

ec2 = boto3.client('ec2')

ig_id='igw-01125b687b468248a'
vpc_id='vpc-0085d19f1a4f831a0'

attachment= ec2.attach_internet_gateway(
    InternetGatewayId=ig_id,
    VpcId=vpc_id
)

