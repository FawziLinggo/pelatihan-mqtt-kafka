import paho.mqtt.client as paho

broker = "broker.mqtt-dashboard.com"
topic = "Temperature"


def on_connect_callback(client, userdata, flags, rc):
    print("connection callback")
    client.subscribe(topic)


client = paho.Client(client_id="subscriber-example-440",
                     transport="tcp",
                     reconnect_on_failure=True
                     )

client.on_connect = on_connect_callback  # assign callback method to on_connect handle
client.connect(broker)


def on_message(client, userdata, message):
    message_data = str(message.payload.decode('utf-8'))  # decode the message that was recieved
    print(f"message = {message_data}")


client.on_message = on_message
client.loop_forever()  # start networking daemon
