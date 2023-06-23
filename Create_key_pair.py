import boto3 
import os

ec2 = boto3.client('ec2')
file_name='PYTHON-BLUETEAM/GLO-keyPair'

response = ec2.create_key_pair(
    KeyName='GLO-Pair',
)

with open (file_name,'w') as f:
    f.write(response["KeyMaterial"])
    
    os.chmod(file_name, 0o400)

