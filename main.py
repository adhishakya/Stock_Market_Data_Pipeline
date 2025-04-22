from app.websocket_listener import WebSocket_Listener

if __name__ == '__main__':
    listener = WebSocket_Listener()
    listener.start()