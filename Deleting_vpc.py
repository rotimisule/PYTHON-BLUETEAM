import boto3
ec2=boto3.client('ec2')

ec2.delete_vpc(
    VpcId='vpc-0085d19f1a4f831a0'
)

