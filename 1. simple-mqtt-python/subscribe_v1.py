import paho.mqtt.client as mqtt
import time
# ym/.#sB*AmZ-H7q


# Method Callback
def on_message(client, userdata,message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "broker.mqtt-dashboard.com"
client = mqtt.Client("Smartphone_indo")
client.connect(mqttBroker)

topic_name = "Temperature"
client.loop_start()
client.subscribe(topic_name)
client.on_message = on_message
time.sleep(30)
client.loop_stop()
