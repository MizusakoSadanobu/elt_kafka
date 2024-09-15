cd kafka_2.13-3.8.0

# Create topic
bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092

# Start producer
bin/kafka-console-producer.sh   --bootstrap-server localhost:9092   --topic news

# create producer
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic bankbranch