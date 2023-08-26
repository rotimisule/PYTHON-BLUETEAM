import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Specify the queue name
queue = 'WAKEUP'

# Create a new queue with specified attributes
response = sqs.create_queue(
    QueueName=queue,
    Attributes={
        'DelaySeconds': '0',          # Message delay before becoming available to consumers
        'VisibilityTimeout': '30',    # Visibility timeout for messages (in seconds)
    }
)

# Extract the QueueUrl from the response
queue_url = response['QueueUrl']

# Print the QueueUrl for the created queue
print("Queue URL:", queue_url)
