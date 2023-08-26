import boto3

ec2 = boto3.client('ec2')
ami_id = "ami-0ccabb5f82d4c9af5"
key = "PYTHON-key"
sg = "sg-0bbcad391c48264e0"


def create_instance(client, ami_id, sg, key, user_data=None, tag_specifications=None):
    response = client.run_instances(
        ImageId=ami_id,
        InstanceType='t2.micro',
        KeyName=key,
        MaxCount=3,
        MinCount=3,
        SecurityGroupIds=[sg],
        UserData=user_data,
        TagSpecifications=tag_specifications  # Corrected placement of TagSpecifications
    )
    print(response["Instances"][0]["InstanceId"])

# Define the TagSpecifications
tag_specifications = [
    {
        'ResourceType': 'instance',
        'Tags': [
            {
                'Key': 'Enviornment',
                'Value': 'Dev',
            },
        ],
    },
]

# Call the create_instance function with the corrected tag_specifications argument
create_instance(ec2, ami_id, sg, key, user_data, tag_specifications)
