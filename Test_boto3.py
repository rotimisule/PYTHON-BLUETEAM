import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
Bucket='rsule-boto3-june122023',##create your bucket name globally unique with a lowercase letter
CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})

print(response)
