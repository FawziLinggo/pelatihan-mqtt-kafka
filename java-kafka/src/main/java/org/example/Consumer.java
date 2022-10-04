package org.example;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.time.Duration;
import java.util.List;
import java.util.Properties;
import java.util.logging.Logger;

public class Consumer {
    public static void main(String[] args) {
        final Logger logger = Logger.getLogger(String.valueOf(Consumer.class));
        try (InputStream input = new FileInputStream
                ("src/main/resources/config.properties")) {

            Properties props = new Properties();
            props.load(input);
            KafkaConsumer<String,String> consumer = new KafkaConsumer<>(props);

            String topic = "producer-java";
            consumer.subscribe(List.of(topic));

            // Pooling
            while (true){
                ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
                for (ConsumerRecord<String,String> record:records){
                    logger.info(" key : " + record.key() +
                                " Value : " + record.value() +
                            " Partitions : " + record.partition() +
                            " Offset : " + record.offset());
                }
            }

        }catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
