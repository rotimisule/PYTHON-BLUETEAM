import boto3

ec2 = boto3.client('ec2')

cidr_block='12.0.2.0/24'
vpc_id='vpc-0085d19f1a4f831a0'

subnet = ec2.create_subnet(CidrBlock=cidr_block,VpcId=vpc_id)

print(subnet["Subnet"]["SubnetId"])