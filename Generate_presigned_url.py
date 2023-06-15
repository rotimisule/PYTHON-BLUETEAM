import boto3 
s3=boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': 'rsule-boto3-june122023','Key': 'Hello_glo.txt'}, ExpiresIn=300)
    
print(response)