from kafka import KafkaProducer, KafkaConsumer

class KafkaConnection:
    def __init__(self, bootstrap_servers='localhost:9092'):
        self.bootstrap_servers = bootstrap_servers

    def create_producer(self):
        return KafkaProducer(bootstrap_servers=self.bootstrap_servers)

    def create_consumer(self, topic, group_id=None, auto_offset_reset='earliest'):
        return KafkaConsumer(
            topic,
            group_id=group_id,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset=auto_offset_reset
        )
