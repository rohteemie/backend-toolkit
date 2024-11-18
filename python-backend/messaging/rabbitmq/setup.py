import pika

class RabbitMQConnection:
    def __init__(self, host='localhost', port=5672, username='guest', password='guest'):
        credentials = pika.PlainCredentials(username, password)
        self.connection_params = pika.ConnectionParameters(host, port, '/', credentials)
        self.connection = None

    def connect(self):
        if not self.connection or self.connection.is_closed:
            self.connection = pika.BlockingConnection(self.connection_params)
        return self.connection

    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
