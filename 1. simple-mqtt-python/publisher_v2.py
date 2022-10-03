import time
import paho.mqtt.client as paho
import random


def on_connect_callback(client, userdata, flags, rc):
    print("connection callback...")


def on_publish_callback(client, userdata, mid):
    print("published data...")


broker = "broker.mqtt-dashboard.com"
topic = "Temperature"

client = paho.Client(client_id="publisher-example-421",
                     transport="tcp",
                     reconnect_on_failure=True
                     )

client.on_connect = on_connect_callback
client.on_publish = on_publish_callback

client.connect(broker)

while True:
    random_number = random.randint(1, 100)
    client.publish(topic, random_number)
    time.sleep(1)