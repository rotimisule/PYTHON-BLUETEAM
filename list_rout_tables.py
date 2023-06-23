import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()
for route in response ["RouteTables"]:
    print(route["VpcId"], route["RouteTableId"] )
    
    for association in route['Associations']:
        print(association['RouteTableAssociationId'])
        if "SubnetId" in association:
            print(association["SubnetId"])
            
            
    for routes in route["Routes"]:
        print(routes["DestinationCidrBlock"], routes["GatewayId"])
  

