import boto3

class SQSConnection:
    def __init__(self, region_name='us-east-1', access_key=None, secret_key=None):
        self.client = boto3.client(
            'sqs',
            region_name=region_name,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )

    def get_queue_url(self, queue_name):
        response = self.client.get_queue_url(QueueName=queue_name)
        return response['QueueUrl']
