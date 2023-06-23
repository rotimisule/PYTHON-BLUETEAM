import boto3 
s3 = boto3.client("s3")

s3.download_file('rsule-boto3-june122023', 'Hello_glo_string.txt', 'PYTHON-BLUETEAM/TEST_Hello_glo_string.txt')


