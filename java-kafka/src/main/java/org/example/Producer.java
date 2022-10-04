package org.example;

import org.apache.kafka.clients.producer.Callback;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Locale;
import java.util.Properties;
import java.util.logging.Logger;

public class Producer {
    public static void main(String[] args) {
        final Logger logger = Logger.getLogger(String.valueOf(Producer.class));
        try (InputStream input = new FileInputStream("src/main/resources/config.properties")) {

            Properties props = new Properties();
            props.load(input);
            KafkaProducer<String,String> producer = new KafkaProducer<>(props);

            for (int i=0;i<10;i++){
                String topic_name ="producer-java";
                String value = "pesan ke - " + Integer.toString(i);
                String key = "key - " + Integer.toString(i);

                // Tidak menggunakan Callback
//                producer.send(new ProducerRecord<>(topic_name, key, value));
//                logger.info("message = " + value);

              ProducerRecord<String,String> record = new ProducerRecord<>(topic_name, key, value);

              producer.send(record, new Callback() {
                    public void onCompletion(RecordMetadata recordMetadata, Exception e) {
                        if (e== null) {
                            logger.info("Successfully received the details as: \n" +
                                    "Topic :" + recordMetadata.topic() + "\n" +
                                    "Partition:" + recordMetadata.partition() + "\n" +
                                    "Offset : " + recordMetadata.offset() + "\n" +
                                    "Timestamp :" + recordMetadata.timestamp() + "\n");
                        }
                        else {
                            logger.warning("Can't produce,getting error " + e);

                        }
                    }
                });
              producer.flush();


            }

        }catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
