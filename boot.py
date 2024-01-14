# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
from machine import Pin, I2C
import micropython
import network
import esp
from test import helloworld
from soilmoisture import read_soil_moisture
# import lcd

def connect_to_wifi():
    ssid = 
    password = 

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Connected to WiFi')
    print('Network config:', wlan.ifconfig())
    return True

broker_address = "192.168.0.211" # Replace with the IP address of the Raspberry Pi
client_id = "ESP32_Subscriber"
topic = "test/topic"

# Callback function to receive messages
def on_message(topic, msg):
    print(f"Received message: {msg} from topic: {topic}")

# Create a new MQTT client instance
client = MQTTClient(client_id, broker_address, keepalive=60)
client.connect()


message = 'hello from ESP32'
# Connect to the broker

client.set_callback(on_message)
# Subscribe to the topic
client.subscribe(topic)
client.publish(topic, message)

print("ESP32 Subscriber connected to MQTT broker, subscribed to topic:", topic)

# Listen for messages
try:
    while True:
        client.check_msg()
        time.sleep(1)
except KeyboardInterrupt:
    client.disconnect()
    print("Subscriber script terminated.")

led = Pin(2, Pin.OUT)

if connect_to_wifi():
    led.on()
else:
    led.off()
