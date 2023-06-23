import boto3 
ec2 = boto3.client('ec2')


instance = ec2.describe_instances()
for reservations in instance ["Reservations"]:
    for instances in reservations ["Instances"]:
        print (instances["InstanceId"], instances["InstanceType"], instances["ImageId"], instances ["VpcId"],
        instances["SubnetId"], instances["State"]["Name"])
        
        if "Tags" in instances:
            for tag in instances ["Tags"]:
                if tag["Key"]=="Name":
                    print(tag["Value"])
                    
        for sg in instances ["SecurityGroups"]:
            print(sg["GroupId"],sg["GroupName"])
            
        
        if "PublicIpAddress" in instances:
            print(instances["PublicIpAddress"])
            
        if "KeyName" in instances:
            print(instances["KeyName"])
            
        if "IamInstanceProfile" in instances:
            print(instances["IamInstanceProfile"]["Id"],instances["IamInstanceProfile"]["Arn"])
        
