from confluent_kafka import Consumer

conf = {'bootstrap.servers': "neo4j:9092",
        'group.id': "foo",
        'enable.auto.commit': False,
        'auto.offset.reset': 'earliest'}

consumer = Consumer(conf)