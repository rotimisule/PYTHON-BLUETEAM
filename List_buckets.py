import boto3  # Importing the Boto3 library for interacting with AWS services

s3 = boto3.client('s3')  # Creating an S3 client object

response = s3.list_buckets()  # Sending a request to list all S3 buckets

buckets = response['Buckets']  # Extracting the list of buckets from the response

for bucket in buckets:
    print(bucket['Name'], bucket['CreationDate'])  # Printing the bucket name and creation date



