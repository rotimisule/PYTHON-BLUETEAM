import boto3

ec2 = boto3.client('ec2')
internet_gateway_id='igw-01125b687b468248a'
vpc_id = 'vpc-0085d19f1a4f831a0'

attachemnt= ec2.detach_internet_gateway(
    InternetGatewayId= internet_gateway_id,
    VpcId=vpc_id
)

