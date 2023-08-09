from confluent_kafka import Producer

# Kafka settings
bootstrap_servers = 'localhost:9092'  # Kafka broker address
topic = 'my-topic'  # Kafka topic name you want to send data to

# Kafka producer configuration
producer_config = {
    'bootstrap.servers': bootstrap_servers
}

# Create Kafka producer
producer = Producer(producer_config)

# Sending data to Kafka topic
for i in range(10):  # Sending 10 messages as an example
    message = f"Message {i}"
    producer.produce(topic, value=message)
    producer.flush()  # Flush to transmit the produced data to the broker

print("Messages sent.")
