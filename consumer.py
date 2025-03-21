from kafka import KafkaConsumer
import json
import logging

logging.basicConfig(level = logging.INFO)

class Consumer:
    consumer = KafkaConsumer(
        'stock_prices',
        bootstrap_servers='localhost:9092',
        auto_offset_reset = 'earliest',
        enable_auto_commit = True,
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    print('Consumer is listening...')

    for message in consumer:
        logging.info('==================================')
        logging.info(f'Received message: {message.value}')