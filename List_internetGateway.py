import boto3

ec2 = boto3.client('ec2')


response = ec2.describe_internet_gateways()


for Id in response['InternetGateways']:
    
    print(Id["InternetGatewayId"])
    for attachment in Id ["Attachments"]:
        print(attachment['VpcId'], attachment["State"])
    for tags in Id['Tags']:
        print(tags['Key'], tags['Value'])
   
