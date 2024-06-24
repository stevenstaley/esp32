from machine import ADC, Pin
import time

# Assuming you're using an ESP32, if not, you might need to adjust this.
# Create an ADC object on GPIO2 (ADC2_CH2)
adc = ADC(Pin(2))

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
    min_val = 3795      # Replace with the value you get when the sensor is in dry soil
    max_val = 3347   # Replace with the value you get when the sensor is in water
    moisture_percentage = ((value - min_val) / (max_val - min_val)) * 100

    # Ensure the percentage is within 0-100% range
    moisture_percentage = max(0, min(100, moisture_percentage))

    return str(moisture_percentage)

while True:
    moisture = read_soil_moisture()
    print("Soil Moisture: {:.0}%".format(moisture))
    time.sleep(1)
