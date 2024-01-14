broker_address = "192.168.0.211" # Replace with the IP address of the Raspberry Pi
client_id = "ESP32_Subscriber"
topic = "test/topic"

# Callback function to receive messages
def on_message(topic, msg):
    print(f"Received message: {msg} from topic: {topic}")

# Create a new MQTT client instance
client = MQTTClient(client_id, broker_address, keepalive=60)
client.connect()

# Connect to the broker

client.set_callback(on_message)
# Subscribe to the topic
while True:
    client.publish(topic)

print("ESP32 Subscriber connected to MQTT broker, subscribed to topic:", topic)

# Listen for messages
try:
    while True:
        client.check_msg()
        time.sleep(1)
except KeyboardInterrupt:
    client.disconnect()
    print("Subscriber script terminated.")
