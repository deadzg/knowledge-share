# Kafka Basics

## Kafka
 - Event Streaming Platform
 - Trillions of events a day
 - Based on distributed commit log
 - Async communication
 - Multiple Producers
 - Multiple consumers
 - Disk-based Retention
 - Scalable
 - High Performance
 
## Usecases
 - Publish + Subscribe
 - Durable storage: Data distribution on multiple nodes for HA
 - Process/Transformation : Manipulate the data as it arrives enabled by Streams API

## Key Points
 
 ### Schema
 	- Avro, JSON, XML
 
 ### Message
 	- Unit of data in Kafka
 	- It's just a byte array to Kafka
 	- Batches
 		- It's a collection of messages, all of which are being produced to the same topic and partition
 		- Compressed for more efficient data transfer and storage at the cost of some processing power
 	- For efficiency messages are written in Kafka in batches
 	- Key
 		- Optional bit of metadata
 		- Similar to message, key is a byte array
 		- Used when messages are written to partition
    - Offset
        - Another bit of metadata
        - Integer value that continually increases
        - Kafka adds to each message as its produced
        - Each message in a given partition has a unique offset
 
 ### Brokers and Clusters
    - Broker
        - A single kafka server
        - Broker receives messages from producers, assigns the offsets and commits the message to storage on disk
        - It services consumers responding to fetch requests for partitions and responding with the messages committed to the disk
    - Kafka brokers are designed to operate in a cluster
    - In a cluster one broker will always function as cluster controller (elected automatically)
    - Controller is responsible for administrative operations, including assigning partitions to brokers, monitoring broker failures...
    - A partition is owned by a single broker in the cluster and that broker is called leader of the partition 
    - A partition may be assigned to multiple brokers thus providing redundancy
    - All consumers and producers must connect to the leaders
    - Multiple Clusters
        - Usecases
            - Segregation of types of data
            - Isolation for security requirements
            - Disaster Recovery

 ### Kafka Clients
 	- Producers (Basic type)
 		- Create new messages
 	- Consumers (Basic type)
 	 	- Reads messages
 	 	- Subscribes to one or more topics
 	 	- Reads messages in order in which they are produced
 	 	- Keep tracks using offset
 	 	- Consumer group
            - One or more consumers that work together to consume a topic
            - Assures that each partition is only consumed by one member
            - If single member fails, the remaining members of the group will rebalance the partitions being consumed
 	- Kafka Connect API (Advanced type)
 	- Kafka Streams (Advanced type)
 	- Advanced clients use producers and consumers as the building blocks for higher level functionality

 - Consumer Groups
 
 ### Topic:
 	- Messages sit in topics
 	- Analogous to table in db or folder in filesystem
 	- Broken down into partitions
 	- Ordering maintained only in a single partition
 	- Partition is a single log
 	- Each partition can be hosted on different server, thus a single topic can be scaled horizontally
    - Retension: Durable storage of messages for some period of time
        - Based on: Time or the space limit of topic
    - Log compacted: Kafka will retain only the last message produced with a specific key. Useful for changelong-type data where only the last update is intresting

 ### Replication
    - Designed to work within single cluster
    - For replicating data between clusters Kafka provides a toll call MirrorMaker (Kafka consumer and producer linked with a queue)

### Misc
 - Retention
 
 - Active-Active/Active-Passive
 - Confluent
 - Connect
 - KSQL
 - Offset
 - Zookeeper
 - Schema Registry
 - Replicator
 - Producer
 - Compression Strategy
 - Streaming
