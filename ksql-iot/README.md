Copy `ksql-udf-deep-learning-mqtt-iot-2.0-jar-with-dependencies.jar` from `ksql-iot/ksql-udf-deep-learning-mqtt-iot-2.0-jar-with-dependencies.jar` 

to the ext folder of your KSQL installation (you will need to create the ext folder)

create folder ext in ksqlDB.
```commandline
cd confluent-7.2.1/etc/ksqldb
mkdir ext
cd ext
```

copy the JAR to `/confluent-5.4.0/etc/ksql/ext`


Set `ksql.extension.dir` in `etc/ksql/ksql-server.properties`:

```commandline
cd ~/confluent-7.2.1
vim etc/ksqldb/ksql-server.properties
vim 
```
ksql.extension.dir=/home/pocneo4j/confluent-7.2.1/etc/ksqldb/ext

## KSQL and Predictions

Start KSQL CLI:
```commandline
ksql http://localhost:8088
```

Confirm that the UDF has been successfully registered (check the KSQL server log if not):
```commandline
ksql> LIST FUNCTIONS;

 Function Name           | Type
-------------------------------------
 ABS                     | SCALAR
 ANOMALY                 | SCALAR
 [...]
```
Register the sensor topic’s schema with KSQL:
```commandline
CREATE STREAM carsensor (eventid integer, sensorinput varchar) WITH (kafka_topic='temperature', value_format='DELIMITED');
```



Set a continuous query running in KSQL:
```commandline
SELECT EVENTID, ANOMALY(SENSORINPUT) FROM CARSENSOR EMIT CHANGES;
```



In KSQL you should see the message displayed with the UDF output:
```commandline
+---------+----------------------+
|EVENTID  |KSQL_COL_0            |
+---------+----------------------+
|99999    |6.997856333119579     |
|99999    |6.03865056857609      |
|99999    |4.691689522784801     |
|99999    |5.6730413613514274    |
|99999    |3.0489548446133092    |
```

Now run a script to generate a stream of MQTT messages:
```commandline
./sensor_generator.sh
```

Now persist the results of the UDF applied to the data, into a new Kafka topic:
```commandline
CREATE STREAM ANOMALYDETECTION AS \
SELECT EVENTID, CAST (ANOMALY(SENSORINPUT) AS DOUBLE) AS ANOMALY_VAL \
FROM   CARSENSOR;
```

From this new stream, create a derived stream that will include only events breaching a given threshold:
```commandline
CREATE STREAM ANOMALYDETECTIONWITHFILTER AS \
SELECT EVENTID, ANOMALY_VAL \
FROM   ANOMALYDETECTION \
WHERE  ANOMALY_VAL > 4;
```

Now you have a KSQL Stream showing breaches where you can create a new SELECT query or CREATE STREAM:
```commandline
ksql> SELECT * FROM ANOMALYDETECTIONWITHFILTER EMIT CHANGES;
```
