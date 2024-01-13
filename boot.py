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

led = Pin(2, Pin.OUT)

if connect_to_wifi():
    led.on()
else:
    led.off()
