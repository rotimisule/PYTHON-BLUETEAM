import boto3

def stop_instance (client, instance_one,instance_two):
    response = client.stop_instances(
        InstanceIds=[
            instance_one,instance_two
    ],
)

def start_instance (client, instance_one, instance_two):
    response = client.start_instances(
        InstanceIds=[
            instance_one,instance_two
    ],
)


def terminate_instances(client, instance_one, instance_two):
    response = client.terminate_instances(
    InstanceIds=[
        instance_one,instance_two
    ],
)



if __name__ =='__main__':
    
    ec2=boto3.client('ec2')
    
    instance_one='i-00516e0045af524db'
    instance_two='i-067761d9f7e3a5aa3'
    
    terminate_instances(ec2, instance_one, instance_two)
    
