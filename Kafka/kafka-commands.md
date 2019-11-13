# Kafka Basic Commands

- Get topic list: `bin/kafka-topics --list --zookeeper localhost:2181`
- Describe topic: `bin/kafka-topics --zookeeper localhost:2181 --describe --topic string_user_topic_dlq`
- Purge a topic: `bin/kafka-topics --zookeeper localhost:2181 --alter --topic string_user_topic_dlq --config retention.ms=1000`
		OR
`kafka-configs.sh --zookeeper localhost:2181 --entity-type topics --alter --entity-name string_user_topic_dlq --add-config retention.ms=1000`

- Delete a topic: `bin/kafka-topics --zookeeper localhost:2181 --delete --topic string_user_topic_dlq`

- Get number of messages in topic: `bin/kafka-run-class kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic 8c7a58db-fcac-451c-b1a1-f857c9a42476 --time -1 --offsets 1 | awk -F ":" '{sum += $3} END {print sum}'`

- CLI Consumer : `bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic 8c7a58db-fcac-451c-b1a1-f857c9a42476`

- CLI Consumer from beginning:`bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic inputTopic --from-beginning`

- CLI Producer: `bin/kafka-console-producer --topic inputTopic --broker-list localhost:9092`

- List consumer groups : `bin/kafka-consumer-groups --list --bootstrap-server localhost:9092`

- Describe consumer group: `bin/kafka-consumer-groups --describe --group 5ab198ab-ae3c-456b-964a-919b72e2ab82 --bootstrap-server localhost:9092`

- Change the broker config in confluent:
`cd /confluent-5.1.0/etc/kafka/server.properties`
Add this at the end of the file: `auto.create.topics.enable=false`

## Schema Registry Commands:

- List all subjects: `curl -X GET http://localhost:8081/subjects`

- List all versions of schema: `curl -X GET http://localhost:8081/subjects/<subject-name>/versions`

- Delete a particular version of Schema: `curl -X DELETE http://localhost:8081/subjects/string_user_topic_dlq-value/versions/1`

## References: 
- https://gist.github.com/ursuad/e5b8542024a15e4db601f34906b30bb5
- https://docs.confluent.io/current/schema-registry/docs/using.html
