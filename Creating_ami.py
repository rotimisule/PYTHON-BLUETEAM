import boto3

ec2=boto3.client("ec2") 

response = ec2.create_image(
    InstanceId='i-07943743f609eb4d6',
    Name='goto-ami',

)

print(response["ImageId"])