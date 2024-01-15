from umqtt.simple import MQTTClient
from machine import ADC, Pin
import time
#from soilmoisture import read_soil_moisture

broker_address = "192.168.0.211" # Replace with the IP address of the Raspberry Pi
client_id = "ESP32_Subscriber"
topic_pub = "publish/esp32"

client = MQTTClient(client_id, broker_address, keepalive=60)
client.connect()

message = 'hello from ESP32 did this change'

while True:
    client.publish(topic_pub, message)
