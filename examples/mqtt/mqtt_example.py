# mqtt_example.py

"""
Example of an MQTT client for loopa.
"""

import paho.mqtt.client as mqtt

class LoopaMQTTClient:
    def __init__(self, broker):
        self.client = mqtt.Client()
        self.client.connect(broker)

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

if __name__ == "__main__":
    client = LoopaMQTTClient("localhost")
    client.publish("test/topic", "Hello, MQTT!")
