import boto3

ec2=boto3.client('ec2')


response = ec2.describe_security_groups()
for sg in response["SecurityGroups"]:
    print (sg["GroupId"], sg["VpcId"], sg ["GroupName"], sg["Description"])
    
    
    for ip in sg ["IpPermissions"]:
        if "FromPort" in ip:
            print (ip["FromPort"])
        
        if "IpProtocol" in ip:
            print(ip["IpProtocol"])
            
        if "ToPort" in ip:
            print (ip["ToPort"])
            
        if "IpRanges" in ip:
            for iprange in ip["IpRanges"]:
                print(iprange["CidrIp"])
  


