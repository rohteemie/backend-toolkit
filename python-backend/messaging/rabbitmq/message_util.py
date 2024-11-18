from rabbitmq.setup import RabbitMQConnection

class RabbitMQUtil:
    def __init__(self, host='localhost', port=5672, username='guest', password='guest'):
        self.connection = RabbitMQConnection(host, port, username, password).connect()
        self.channel = self.connection.channel()

    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)

    def publish_message(self, queue_name, message):
        self.declare_queue(queue_name)
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print(f"Message published to {queue_name}: {message}")

    def consume_messages(self, queue_name, callback):
        self.declare_queue(queue_name)
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        print(f"Consuming messages from {queue_name}...")
        self.channel.start_consuming()

    def close(self):
        self.connection.close()
