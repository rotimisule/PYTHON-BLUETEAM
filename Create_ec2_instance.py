import boto3


ec2=boto3.client('ec2')
ami_id="ami-024e6efaf93d85776"
key="GLO-Pair"
sg="sg-0b285d2deaab69a7e"

user_data= '''#!/bin/bash
    apt update-y
    apt -get install -y apache2
    systemctl start apache
    systemctl enable apache2'''



def create_instance(client , ami_id, sg, key, user_data=None):

    response = client.run_instances(
      
        ImageId=ami_id,
        InstanceType='t2.micro',
        KeyName=key,
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            sg,
        ],
        UserData=user_data
      
    )
    print(response["Instances"][0]["InstanceId"])
    
create_instance(ec2, ami_id, sg,key, user_data)

    


    