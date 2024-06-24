import dht
import machine
import esp32

d = dht.DHT11(machine.Pin(4))
d.measure()
t = d.temperature()
h = d.humidity()
f = (t * 1.8) + 32
espt = esp32.raw_temperature()

print("The temperature is " + str(f))
print("The humidity is " + str(h))
print("The ESP's temperature is " + str(espt))