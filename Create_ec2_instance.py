import boto3
ec2=boto3.client('ec2')
ami="ami-0996a91449839b5c2"
key="GLO-Pair"
sg="sg-0b285d2deaab69a7e"

response = ec2.run_instances(
  
    ImageId=ami,
    InstanceType='t2.micro',
    KeyName=key,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        sg,
    ],
  
)

print(response["Instances"][0]["InstanceId"])