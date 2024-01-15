import paho.mqtt.client as mqtt
import time

# Setup the connection information
broker_address = "192.168.0.211" # Use the IP address of the Raspberry Pi
port = 1883
topic_pub = "test/topic"
topic_sub = "publish/esp32"


# Publish messages in a loop
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic_sub)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

 
# Create an MQTT client and attach our routines to it.
# Create a new MQTT client instance
client = mqtt.Client("RaspberryPi_Publisher")
client.on_connect = on_connect
client.on_message = on_message
# Connect to the broker
client.connect(broker_address, port=port)

client.loop_forever()
