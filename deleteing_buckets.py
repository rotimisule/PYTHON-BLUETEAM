import boto3 

s3 =boto3.client('s3')

bucket = 'rsule-boto3-june122023'

response = s3.delete_bucket(
    Bucket=bucket
    )