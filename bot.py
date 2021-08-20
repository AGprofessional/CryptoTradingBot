#import websocket
import websocket

EXAMPLE = "wss://stream.binance.com:9443/ws/<streamName>/"
#where <streamName> is <symbol>@kline_<interval>

SOCKET = "wss://stream.binance.com:9443/ws/ethusd@kline_1m"



def on_open():
    print("connection opened")

def on_closed():
     print("connection closed")

def on_message():
     print("received payload message")

ws = websocket.WebsocketApp(SOCKET, on_open = on_open, on_closed=on_closed, on_message=on_message)