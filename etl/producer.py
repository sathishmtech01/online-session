import json
import time
import random
from kafka import KafkaProducer
import json
# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Open and read the JSON file
with open('input/sensor.json', 'r') as file:
    input_data = json.load(file)
# Sample data to send to Kafka
def produce_data():
    while True:
        data = {
            'sensor_id': random.randint(input_data['sensor_id']['min'], input_data['sensor_id']['max']),
            'temperature': random.uniform(input_data['temperature']['min'], input_data['temperature']['max']),
            'humidity': random.uniform(input_data['humidity']['min'], input_data['humidity']['max']),
            'timestamp': time.time()
        }
        producer.send('test-topic', value=data)
        print(f"Sent: {data}")
        time.sleep(1)

if __name__ == "__main__":
    produce_data()
