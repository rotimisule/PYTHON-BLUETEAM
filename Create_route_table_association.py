import boto3

ec2 = boto3.client('ec2')
route_table_id='rtb-0b54f55a055bb05bf'
subnet_id='subnet-029bea8ffdce41e6d'

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id
)

print(association['AssociationId'])


