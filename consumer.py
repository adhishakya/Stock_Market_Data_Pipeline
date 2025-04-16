from kafka import KafkaConsumer
import psycopg2
import json
import logging
from dotenv import load_dotenv
import os

load_dotenv()
logging.basicConfig(level = logging.INFO)

db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

conn = psycopg2.connect(
    dbname = db_name,
    user = db_user,
    password = db_password,
    host = db_host,
    port = db_port
)
cursor = conn.cursor()

kafka_consumer =  KafkaConsumer(
    'stock_prices',
    bootstrap_servers = 'localhost:9092',
    auto_offset_reset = 'earliest',
    enable_auto_commit = True,
    value_deserializer = lambda m: json.loads(m.decode('utf8'))
)

logging.info('Kafka consumer is listening on stock data...')

for message in kafka_consumer:
    try:
        stock_data = message.value
        logging.info(f'Received message: {stock_data}')

        json_stock_data = json.loads(stock_data)
        if isinstance(json_stock_data,dict) and 'data' in json_stock_data:
            for data in json_stock_data['data']:
                symbol = data.get('s')
                last_price = data.get('p')
                volume = data.get('v')
                trade_timestamp = data.get('t')

                file = open('insert_query.sql','r')
                query = file.read()
                values = (symbol, last_price, volume, trade_timestamp)

                cursor.execute(query,values)
                conn.commit()
                logging.info('Data inserted into PostgreSQL')

    except Exception as e:
        logging.error(f'An error occurred: {e}')

cursor.close()
conn.close()