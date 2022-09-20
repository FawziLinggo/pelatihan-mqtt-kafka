# Must Install Connector
#Use the Confluent Hub client to install this connector with:
confluent-hub install confluentinc/kafka-connect-mqtt:1.5.2

# Create Connector using REST API
curl -s -X POST -H 'Content-Type: application/json' http://localhost:8083/connectors -d '{
"name" : "Tes-mqtt-souce-kafka",
"config" : {
  "connector.class" : "io.confluent.connect.mqtt.MqttSourceConnector",
  "tasks.max" : "1",
  "mqtt.server.uri" : "tcp://localhost:1883",
  "mqtt.topics" : "Temperature",
  "kafka.topics" : "Temperature"
  }
}'


# if u using ubuntu please install mqtt borker first
# Link : https://www.vultr.com/docs/install-mosquitto-mqtt-broker-on-ubuntu-20-04-server/