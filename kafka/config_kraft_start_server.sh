cd kafka_2.13-3.8.0

# Generate a cluster UUID that will uniquely identify the Kafka cluster.
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

# Configure the log directories passing the cluster ID because KRaft requires the log directories to be configured.
bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties

# Start Kafka cluster
bin/kafka-server-start.sh config/kraft/server.properties