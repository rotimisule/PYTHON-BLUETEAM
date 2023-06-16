import boto3

s3 = boto3.client('s3')

s3.upload_file('PYTHON-BLUETEAM/Hello_glo.txt', 'rsule-boto3-june122023','Hello_glo_upload.txt',ExtraArgs={'ContentType':"text/plain"} )
