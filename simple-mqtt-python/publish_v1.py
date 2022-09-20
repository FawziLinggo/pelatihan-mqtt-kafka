import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

# Connect to mqtt Broker
#
# mqttBroker = "neo4j"
mqttBroker = "mqtt.eclipseprojects.io"

# client_name
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

#topic name
topic_name = "Temperature"

while True:
    randNumber = int(uniform(50, 100))
    client.publish(topic_name, randNumber)
    print("published " + str(randNumber) + " to Topic " + topic_name)
    time.sleep(1)