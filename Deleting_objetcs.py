import boto3
s3 = boto3.client('s3')

bucket = 'rsule-boto3-june122023'
key = "Hello_glo_string.txt"

keys= ['Hello_glo_upload.txt', 'Hello_glo.txt']#listing the objects that you may want to delete

def delete_object(cliebt, bucket, key):
    response = s3.delete_object(
    Bucket = bucket,
    Key=key
    
    )
    return response
    
    
def delete_object_2 (client , bucket , keys):
    objects =[{"Key" : key }for key in keys ]
    
    response = client.delete_objects(
    Bucket=bucket,
    Delete={
        'Objects': objects
        }
         
        )
    return response 
       
    
delete_object_2(s3,bucket,keys)
    