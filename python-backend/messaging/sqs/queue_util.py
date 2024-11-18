from sqs.setup import SQSConnection

class SQSUtil:
    def __init__(self, region_name='us-east-1', access_key=None, secret_key=None):
        self.connection = SQSConnection(region_name, access_key, secret_key)

    def send_message(self, queue_name, message):
        queue_url = self.connection.get_queue_url(queue_name)
        self.connection.client.send_message(QueueUrl=queue_url, MessageBody=message)
        print(f"Message sent to {queue_name}: {message}")

    def receive_messages(self, queue_name, max_messages=10):
        queue_url = self.connection.get_queue_url(queue_name)
        response = self.connection.client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=max_messages
        )
        messages = response.get('Messages', [])
        for message in messages:
            print(f"Received message: {message['Body']}")
            self.connection.client.delete_message(
                QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle']
            )
        return messages
