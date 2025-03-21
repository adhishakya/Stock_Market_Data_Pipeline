from dotenv import load_dotenv
import websocket
from producer import Producer
import os
import logging

logging.basicConfig(level = logging.INFO)

class WebSocket_Listener:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('TOKEN')
        self.url = os.getenv('URL')
        self.topic_name = os.getenv('TOPIC_NAME')

        self.producer = Producer()

        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            self.url + self.token,
            on_message = self.on_message,
            on_error = self.on_error,
            on_close = self.on_close
        )
        self.ws.on_open = lambda ws:self.on_open(ws)

    def on_message(self, ws, msg):
        logging.info(msg)
        self.producer.producer_listener().send(self.topic_name,value = msg)
        self.producer.producer_listener().flush()

    def on_error(self, ws, err):
        logging.info(f'An error occurred {err}')

    def on_close(self, ws):
        logging.info('Connection closed')

    def on_open(self,ws):
        ws.send('{"type":"subscribe","symbol":"AAPL"}')
        ws.send('{"type":"subscribe","symbol":"AMZN"}')
        ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
        ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')

    def start(self):
        self.ws.run_forever()