import boto3

ec2 = boto3.client('ec2')
route_table_id = 'rtb-0b54f55a055bb05bf'
internet_gateway_id='igw-01125b687b468248a'


route = ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)

