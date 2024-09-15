cd kafka_2.13-3.8.0

# create bank topic
bin/kafka-topics.sh --create --topic bankbranch --partitions 2 --bootstrap-server localhost:9092

# List all topics to check if bankbranch has been created successfully.
bin/kafka-topics.sh --bootstrap-server localhost:9092 --list

# check the details of the topic bankbranch
bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic bankbranch