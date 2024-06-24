# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from umqtt.simple import MQTTClient
import network
import time
from machine import ADC, Pin
import dht

# Function to connect to Wi-Fi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.active(True)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Connected to WiFi')
    print('IP Address:', wlan.ifconfig()[0])

# Replace 'your_wifi_ssid' and 'your_wifi_password' with your actual Wi-Fi credentials
wifi_ssid = ""
wifi_password = ""

led = Pin(2, Pin.OUT)
# Connect to Wi-Fi on boot
connect_wifi(wifi_ssid, wifi_password)
#     while True:
#         led.on()
#         time.sleep(0.5)
#         led.off()
#         time.sleep(2.9)
        



# from umqtt.simple import MQTTClient
# from machine import ADC, Pin
# import time
# import dht
#from soilmoisture import read_soil_moisture



# while True:
#     broker_address = "192.168.0.211" # Replace with the IP address of the Raspberry Pi
#     client_id = "ESP32_Device"
#     topic_t = "homeassistant/publish/temperature"
#     topic_h = "homeassistant/publish/humidity"
#     client = MQTTClient(client_id, broker_address)
#     client.connect()
#     d = dht.DHT11(Pin(4))
#     d.measure()
#     t = d.temperature()
#     h = d.humidity()
#     f = (t * 1.8) + 32
#     client.publish(topic_t, str(float(f)))
#     print(f)
#     client.publish(topic_h, str(h))
#     print(h)
#     print("Message Published")
#     time.sleep(5)

