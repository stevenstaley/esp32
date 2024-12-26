import dht
import machine
import esp32
import time
from bmp180 import BMP180
from machine import SoftI2C, Pin
from umqtt.simple import MQTTClient

# create an I2C bus object accordingly to the port you are using
# bus = I2C(1, baudrate=100000)           # on pyboard
def read_pressure():
    bus =  SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)   # on esp8266
    bmp180 = BMP180(bus)
    bmp180.oversample_sett = 2
    bmp180.baseline = 101325

    # temp = bmp180.temperature
    p = bmp180.pressure
    milli = p / 100
    inhg = milli / 33.8639
    formatinhg = "{:.2f}".format(inhg)
# altitude = bmp180.altitude
    return formatinhg



while True:
    d = dht.DHT11(machine.Pin(4))
    d.measure()
    t = d.temperature()
    h = d.humidity()
    f = (t * 1.8) + 32
    espt = esp32.raw_temperature()

    print("The temperature is " + str(f))
    print("The humidity is " + str(h))
    print("The ESP's temperature is " + str(espt))
    presh = read_pressure()
    print(presh)
    time.sleep(2)
    


 



while True:
    broker_address = "192.168.0.211" # Replace with the IP address of the Raspberry Pi
    client_id = "ESP32_Device"
    topic_esp_temp = "esp32/internaltemp"
    topic_t = "homeassistant/publish/temperature"
    topic_h = "homeassistant/publish/humidity"
    topic_soil = "homeassistant/publish/soilmoisture"
    client = MQTTClient(client_id, broker_address)
    client.connect()
    esp_temp = esp32.raw_temperature()
    d = dht.DHT11(Pin(4))
    try:
        d.measure()
    except OSError as e:
        print("Messed up")
    pass
    t = d.temperature()
    h = d.humidity()
    f = (t * 1.8) + 32
    client.publish(topic_t, str(float(f)))
    client.publish(topic_h, str(h))
    client.publish(topic_esp_temp, str(esp_temp))
    led = Pin(2, Pin.OUT)
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    moisture = read_soil_moisture()
    client.publish(topic_soil, str(moisture))
    time.sleep(3)

