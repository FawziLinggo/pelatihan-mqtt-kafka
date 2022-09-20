## Connect Mqtt Kafka

This note shows an example of Internet of Things (IoT) integration using Apache Kafka + Kafka Connect + MQTT Connector + Sensor Data.

### Architecture: Sensor Data via MQTT Broker and Kafka Connect MQTT Connector to Kafka Cluster

![](images/Apache_Kafka_Connect_MQTT_Broker_Mosquitto_Integration.png)

As an alternative to using Kafka Connect, you can also take advantage of MQTT Confluent Proxy to integrate IoT data from IoT devices directly without needing an MQTT Broker

### Check Status of Connector

```bash
# using // REST
curl -s "http://localhost:8083/connectors"
curl -s "http://localhost:8083/connectors/Tes-mqtt-souce-kafka/status"
curl -s -X DELETE localhost:8083/connectors/Tes-mqtt-souce-kafka
```

### Create Topic

Next, create a Kafka Topic for consuming the MQTT messages via the MQTT Connector (needs to be the same as in the Connector Config):

hmm, I think if u using default config confluent, auto create topic is enabled :)

```commandline
kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic mqtt
```

lets pub the message 
```commandline
mosquitto_pub -h neo4j -p 1883 -t Temperature -q 2 -m "312332111,2.10#"
```


## Rest Kafka Mqtt
go to path :

```commandline
cd ~/confluent-7.2.1/etc/confluent-kafka-mqtt
kafka-mqtt-start kafka-mqtt-start kafka-mqtt-dev.properties
```

so we have run rest mqtt. next we will try to do streaming processing using ksqldb