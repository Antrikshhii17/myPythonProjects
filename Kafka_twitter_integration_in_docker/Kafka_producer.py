from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})
msg = ('We are testing our kafka pipeline' * 20).encode()[:100]
size = 100000


def confluent_producer01():
    for word in range(size):
        producer.produce(
            "topic01",
            msg
        )
    producer.flush()

