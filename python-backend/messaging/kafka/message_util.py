from kafka.setup import KafkaConnection

class KafkaUtil:
    def __init__(self, bootstrap_servers='localhost:9092'):
        self.connection = KafkaConnection(bootstrap_servers)

    def send_message(self, topic, message):
        producer = self.connection.create_producer()
        producer.send(topic, message.encode('utf-8'))
        producer.flush()
        print(f"Message sent to topic {topic}: {message}")

    def consume_messages(self, topic, group_id=None, callback=None):
        consumer = self.connection.create_consumer(topic, group_id)
        print(f"Listening for messages on topic {topic}...")
        for message in consumer:
            if callback:
                callback(message)
            else:
                print(f"Received message: {message.value.decode('utf-8')}")
