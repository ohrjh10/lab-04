import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

def on_connect(client, userdata, flags, rc):
    print("Connected to server with result code "+str(rc))

    client.subscribe("ohr/pong")
    client.message_callback_add("ohr/pong", on_message_from_pong)

def on_message_from_pong(client, userdata, message):
    x = int(message.payload.decode()) +1
    print("Custom callback - ping: ", x)
    time.sleep(1)
    client.publish("ohr/ping", x)
    
if __name__ == '__main__':
    ip_address="172.20.10.4"
    client = mqtt.Client()

    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host= ip_address, port=1883, keepalive=60)
    client.loop_start()
    
    time.sleep(1)
    x = 0
    client.publish("ohr/pong",x)
    print("Publishing pong")

    while True:
        pass
