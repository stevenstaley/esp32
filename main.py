from umqtt.simple import MQTTClient
from machine import ADC, Pin
import time
import dht
#from soilmoisture import read_soil_moisture

while True:
    broker_address = "192.168.0.211" # Replace with the IP address of the Raspberry Pi
    client_id = "ESP32_Device"
    topic_t = "homeassistant/publish/temperature"
    topic_h = "homeassistant/publish/humidity"
    client = MQTTClient(client_id, broker_address)
    client.connect()
    
    d = dht.DHT11(Pin(4))
    time.sleep(0.5)
    try:
        d.measure()
    except OSError as e:
        print("Messed up")
    pass
    t = d.temperature()
    h = d.humidity()
    f = (t * 1.8) + 32
    client.publish(topic_t, str(float(f)))
    print(f)
    client.publish(topic_h, str(h))
    print(h)
    print("Message Published")
    led = Pin(2, Pin.OUT)
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)

