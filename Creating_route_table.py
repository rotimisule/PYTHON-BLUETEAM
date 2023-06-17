import boto3

ec2= boto3.client('ec2')

vpc_id='vpc-0085d19f1a4f831a0'


routeTable= ec2.create_route_table(
    VpcId=vpc_id
)

print(routeTable["RouteTable"]["RouteTableId"])