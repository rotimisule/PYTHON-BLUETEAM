import boto3

ec2 = boto3.client('ec2')
routeTableId = 'rtb-0b54f55a055bb05bf'

response = ec2.describe_route_tables(
    RouteTableIds=[routeTableId],
        
    
    )
    
    
for association in response["RouteTables"][0]["Associations"]:
    if not association["Main"]:
        association_id = association["RouteTableAssociationId"]
        print(association_id)
        ec2.disassociate_route_table(
            AssociationId=association_id
)

