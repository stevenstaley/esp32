import paho.mqtt.client as mqtt
import time

# Setup the connection information
broker_address = "192.168.0.211" # Use the IP address of the Raspberry Pi
port = 1883
topic = "test/topic"

# Create a new MQTT client instance
client = mqtt.Client("RaspberryPi_Publisher")

# Connect to the broker
client.connect(broker_address, port=port)

# Publish messages in a loop
try:
    while True:
        message = "Hello from Raspberry Pi!"
        client.publish(topic, message)
        print(f"Message sent: {message}")
        time.sleep(5) # Wait for 5 seconds before the next send
except KeyboardInterrupt:
    print("Publisher script terminated.")