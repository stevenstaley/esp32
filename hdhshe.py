
import paho.mqtt.client as mqtt
import time

# Define the MQTT settings
MQTT_BROKER = "broker.hivemq.com"  # Replace with your MQTT broker
MQTT_PORT = 1883                    # Default MQTT port

# Global variable to store the message
received_message = None

# Callback function on message receipt
def on_message(client, userdata, message):
    global received_message
    received_message = message.payload.decode()  # Decode the message payload

def subscribe_to_topic(topic):
    global received_message
    received_message = None  # Reset the message

    # Create an MQTT client instance
    client = mqtt.Client()

    # Attach the on_message callback function
    client.on_message = on_message

    # Connect to the MQTT broker
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # Subscribe to the specified topic
    client.subscribe(topic)

    # Start the MQTT client loop
    client.loop_start()

    try:
        print(f"Subscribed to topic '{topic}'. Waiting for messages...")
        
        # Wait for a message to be received
        while received_message is None:
            time.sleep(1)  # Sleep to avoid busy waiting

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        # Stop the loop and disconnect
        client.loop_stop()
        client.disconnect()

    return received_message

# Example usage
if __name__ == "__main__":
    topic = "your/topic"  # Replace with your topic
    message = subscribe_to_topic(topic)
    print(f"Received message: {message}")
