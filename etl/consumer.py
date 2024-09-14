import time

from kafka import KafkaConsumer
import csv
import ast
from datetime import datetime
from transform import check_temperature_and_humidity

# csv_file = 'output/sensor_data_'+str(formatted_time)+'.csv'
# Create Kafka Consumer
consumer = KafkaConsumer(
    'vit-demo',                      # Topic to subscribe to
    bootstrap_servers=['localhost:9092'],  # Kafka broker(s)
    auto_offset_reset='earliest',     # Start from the earliest available message
    enable_auto_commit=True,          # Enable auto-commit of offsets
    group_id='my-consumer-group',     # Consumer group ID
    value_deserializer=lambda x: x.decode('utf-8')  # Deserialize message value from bytes to string
)

# Initialize record counter and file index
record_count = 0
file_index = 1

# Function to get new file name based on file index
def get_new_file_name():

    # Get current date and time with seconds
    current_time = datetime.now()

    # Format the datetime to include seconds
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    return f'output/sensor_data_'+str(formatted_time)+'.csv'

# Open the first CSV file
file_name = get_new_file_name()
print(file_name)
csv_file = open(file_name, mode='w', newline='')
csv_writer = csv.writer(csv_file)


try:
    # Extract
    for message in consumer:
        # Assuming the Kafka message is a comma-separated string
        data = ast.literal_eval(message.value)
        # row values ['topic', 'partition', 'offset','sensor_id','timestamp','temperature','humidity','outcome']

        # Transform
        row_value = [message.topic, message.partition, message.offset,data['sensor_id'],data['timestamp'],
                     data['temperature'],data['humidity'],check_temperature_and_humidity(data['temperature'],data['humidity'])]

        # Load
        # Write the row to the current CSV file
        csv_writer.writerow(row_value)
        print(f"Written to CSV: {row_value}")
        record_count += 1

        # If 20 records are written, close the current file and open a new one
        if record_count == 100:
            # Close the current file
            csv_file.close()

            # Increment file index and reset record count
            file_index += 1
            record_count = 0

            # Open a new CSV file and write the header again
            file_name = get_new_file_name()
            print(file_name)
            csv_file = open(file_name, mode='w', newline='')
            csv_writer = csv.writer(csv_file)

except KeyboardInterrupt:
    print("Consumer interrupted by user")

finally:
    # Close the file before exiting
    csv_file.close()

