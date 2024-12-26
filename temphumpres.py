import dht
import machine
import esp32
import time
from bmp180 import BMP180
from machine import SoftI2C, Pin

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

