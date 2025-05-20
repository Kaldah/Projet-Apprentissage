import websocket
import json
import time

def on_message(ws, message):
    print("Received:", message)

def on_open(ws):
    # Move forward for 1 second
    ws.send(json.dumps({"action": "move", "value": True}))
    time.sleep(1.2)

    # Jump
    ws.send(json.dumps({"action": "jump"}))
    time.sleep(0.7)

    # Look around: yaw=90°, pitch=0°
    ws.send(json.dumps({"action": "look", "yaw": 1.57, "pitch": 0}))
    time.sleep(1)

    # Request blocks in front
    ws.send(json.dumps({"action": "getBlocks"}))

def on_error(ws, error):
    print("Error:", error)

def on_close(ws):
    print("Connection closed")

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://localhost:8080/",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
