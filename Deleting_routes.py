import boto3 

ec2= boto3.client('ec2')
route_table_id='rtb-0b54f55a055bb05bf'

route = ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=route_table_id
)

