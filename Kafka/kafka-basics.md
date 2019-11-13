# Kafka Basics

## Kafka
 - Event Streaming Platform
 - Trillions of events a day
 - Based on distributed commit log
 - Async communication
 
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

 ### Kafka Clients
 	- Producers (Basic type)
 		- Create new messages
 	- Consumers (Basic type)
 	 	- Reads messages
 	 	- Subscribes to one or more topics
 	 	- Reads messages in order in which they are produced
 	 	- Keep tracks using offset
 	 	
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

### Misc
 - Retention
 - Replication
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
