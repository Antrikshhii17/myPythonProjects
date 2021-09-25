from confluent_kafka import Consumer

consumer = Consumer(
    {
        'bootstrap.servers': 'localhost:9092',
        'auto.offset.reset': 'earliest'
    }
)
consumer.subscribe(['topic01'])


def confluent_consumer():
    consumer.subscribe(['topic01'])

