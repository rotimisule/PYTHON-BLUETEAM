import boto3

ec2= boto3.client('ec2')

ec2.delete_subnet(
    SubnetId='subnet-029bea8ffdce41e6d'


)

