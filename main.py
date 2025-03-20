import websocket
from dotenv import load_dotenv
import os

def on_message(ws, msg):
    print(msg)

def on_error(ws, err):
    print(err)

def on_close(ws):
    print('Connection closed!')

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')

if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TOKEN')
    url = os.getenv('URL')
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        url+token,
        on_message =on_message,
        on_error = on_error,
        on_close = on_close
    )
    ws.on_open = on_open
    ws.run_forever()