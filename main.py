from umqtt.simple import MQTTClient
from machine import ADC, Pin
import time
import dht
import esp32

adc = ADC(Pin(35))
# Configure the ADC resolution and attenuation
# ESP32 supports up to 12 bits resolution.
adc.width(ADC.WIDTH_12BIT)
# For full range of input voltage (0v - 3.3v) in ESP32 use ADC.ATTN_11DB
# Adjust the attenuation according to your sensor specification and application.
adc.atten(ADC.ATTN_11DB)

# Function to read and convert the soil moisture value
def read_soil_moisture():
    # Read the ADC value
    value = adc.read()
    # Convert the ADC value to percentage (assuming a linear response and 3.3V ADC reference)
    # You might need to calibrate these values depending on your sensor's output range.
    min_val = 4095      # Replace with the value you get when the sensor is in dry soil
    max_val = 3294   # Replace with the value you get when the sensor is in water
    moisture_percentage = ((value - min_val) / (max_val - min_val)) * 100
    # Ensure the percentage is within 0-100% range
    moisture_percentage = max(0, min(100, moisture_percentage))
    return moisture_percentage


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

