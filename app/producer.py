from kafka import KafkaProducer
import json

class Producer:
    def producer_listener(self):
        return KafkaProducer(
            bootstrap_servers = 'localhost:9092',
            value_serializer = lambda v: json.dumps(v).encode('utf-8')
        )

