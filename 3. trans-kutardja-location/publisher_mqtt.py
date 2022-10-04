import uuid
import paho.mqtt.client as mqtt

import json
from datetime import datetime
import time

# READ COORDINAT FROM GEOJSON
input_file = open("/Users/All Data Int/pelatihan-mqtt-kafka/3. trans-kutardja-location/location/transkutaraja_1.json")
json_array = json.load(input_file)
coordinates = json_array['features'][0]['geometry']['coordinates']


def generate_uuid():
    return uuid.uuid4()


# CONSTRUCT MESSAGE AND SEND IT TO MQTT
data = {}
data['kutardaja'] = 'BL 1234 Q'

# client_name
mqttProxy = "neo4j"
client = mqtt.Client("Temperature")

# topic name
topic_name = "transkutaradja_location.pelatihan"

client.connect(mqttProxy, port=1882)


def generate_checkpoint(coordinates):
    i = 0
    while i < len(coordinates):
        data['key'] = data['kutardaja'] + '_' + str(generate_uuid())
        data['timestamp'] = str(datetime.utcnow())
        data['latitude'] = coordinates[i][1]
        data['longitude'] = coordinates[i][0]
        message = json.dumps(data)
        print(message)
        client.publish(topic_name, message)
        time.sleep(1)

        # if bus reaches last coordinate, start from beginning
        if i == len(coordinates) - 1:
            i = 0
        else:
            i += 1


generate_checkpoint(coordinates)
