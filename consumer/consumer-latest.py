from confluent_kafka import Consumer, KafkaError
import time

def kafka_settings():
    # Kafka settings
    bootstrap_servers = 'localhost:9092'  # Kafka broker address
    topic = 'my-topic'  # Kafka topic name you want to consume from
    return topic,bootstrap_servers

def consumer_config(bootstrap_servers):
    # Kafka consumer configuration
    return {
        'bootstrap.servers': bootstrap_servers,
        'group.id': 'my-consumer-group-latest',  # Consumer group ID
        'auto.offset.reset': 'latest'   # Start consuming from the beginning of the topic
    }

def main_consumer_latest():
    topic,bootstrap_servers = kafka_settings()

    # Create Kafka consumer
    consumer = Consumer(consumer_config(bootstrap_servers))
    
    # Subscribe to the Kafka topic
    consumer.subscribe([topic])

    # Consume messages from the topic
    try:
        while True:
            msg = consumer.poll(1.0)  # Poll for messages with a timeout of 1 second
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
            else:
                print(f"Received message: {msg.value().decode('utf-8')}")
                time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

main_consumer_latest()