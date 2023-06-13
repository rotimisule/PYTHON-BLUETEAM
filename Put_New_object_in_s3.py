import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket="rsule-boto3-june122023", Key="Hello_glo_string.txt", Body="Hey this is Sir GLo", ContentType="text/plain")
    
