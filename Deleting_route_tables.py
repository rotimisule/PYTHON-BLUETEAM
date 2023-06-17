import boto3

ec2= boto3.client('ec2')

delete= ec2.delete_route_table(
    RouteTableId='rtb-0b54f55a055bb05bf',
)

print(delete)


