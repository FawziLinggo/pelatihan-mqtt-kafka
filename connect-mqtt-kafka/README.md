## Connect Mqtt Kafka

This note shows an example of Internet of Things (IoT) integration using Apache Kafka + Kafka Connect + MQTT Connector + Sensor Data.

### Architecture: Sensor Data via MQTT Broker and Kafka Connect MQTT Connector to Kafka Cluster

![](/home/adi/fawzi_linggo/pelatihan-mqtt-kafka/images/Apache_Kafka_Connect_MQTT_Broker_Mosquitto_Integration.png)

As an alternative to using Kafka Connect, you can also take advantage of MQTT Confluent Proxy to integrate IoT data from IoT devices directly without needing an MQTT Broker