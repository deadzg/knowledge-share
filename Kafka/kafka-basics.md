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

 ## Business Usecases
 - Activity Tracking
 - Send notification
 - Metrics and Logging
 - Commit Log
 - Stream processing

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
 ### Producers
 - Post send the ProducerRecord, the producer will serialize the key and value objets into ByteArray so it can send over network
- Partitioner return the Partition specified or choose bsed on the Key specified
- Post determining topic,partition , it adds the record to a batch of records that will be sent to same (topic,partition)
- A separate thread is responsible for sending the batches of records to the appropriate Kafka brokers
- If success, Broker send RecordMetadata obj with topic, partition and the offset of the record within the partition

*Key Properties for Constructing Producer*
- bootstrap.servers
- key.serializer
- value.serializer

*Key Params* which can have significant impact on memory use, performance and reliability of the producers:
- acks:
	How many partition replicas must recieve the record before the producer can consider the write successful
	0: 
		- Producer wont wait for reply. 
		- It can send messages as fast as the network will support
		- Used for acheiving high throughput

	1:
		- In this case the throughput depends on we send record sync or async

	all:
		- Producer receives success when all in-sync replicas received the message
		- Safest method to make sure more than one broker has the message
		- Latency will be higher since we wait for more than one broker to receive the message

- buffer.memory:
- compression.type:
	- Default uncompressed
	- Reduce n/w utilization and storage
	- snappy/gzip/lz4
	- snappy : recommneded for both performance and bandwidth because of low CPU overhead
	- gzip : More CPU and time but better compression ratios. Better for restricted network bandwidth 
- retries
- batch.size
	- Setting the batch size too large will not cause delays and it can send half batch size or even batches with single message driven by linger.ms param
	- Setting it too small, will result in adding some overhead as producer had to sned messages more frequnetly
-linger.ms
	- Amount of time to wait for additional messges before sending the current batch
	- Increases latency but also increase throghput (we send more messages at once, there is less overhead per message)
- client.id 
	- Used by broker to identify messages sent from the client
- max.request.size
	- Controls the size of a produce req sent by producer
	- It caps both the size of the largest message sent and the number of messages that the producer can send in one req
- reciever.buffer.bytes & send.buffer.bytes
	- Size of the TCp send and receive buffers used by the sockets when writiing and reading data
	- Increase those when prod/cons communicate with brokers in a different datacenter because those network links typically have higer latency and lower bandwidth

*Primary methods for Sending Message*
- Fire and forget send
	- Don't really care if it arrives successfully or not
- Synchronous send
	- send() return Future object, and we use get() to wait on the future and see if send() was success or not
- Asynchronous send
	- send() method with a callback function, which gets triggered when it receives a response from broker
	- Faster as we are not waiting for the replies from broker


*KafkaProducer has two types error*
- Retriable errors can be resolved by sending the message again. Eg: Connection Error, No Leader

- Non Retireable Errors: Eg Message size too large. Will not try in this case and returns error

#### Key Desgin Consideration for Producer:
- For better throughput, add more threads that use the same producer
- Once thread ceases to increase throughput, you can add more producers to achieve even higher throughput
- Select right acks setting	
- Choose correct key for partitioning or use Custom Partitioning Strategy (Eg: One customer is much biger than rest, so you can handle it in separate partition)

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
 
### Consumers
- Consumer Group: When multiple consumers are subscribed to a topic and belong to the same consumer group, each consumer in the group will receive msgs from a different subset of the partition in the topic
- Can add multiple CG to topic which read the msgs independently
- Rebalancing: Moving partitions ownership from one consumer to another. It provides HA and scalability
	- Reasons:
		- New consumer added in CG
		- Topic is modified by admin by adding new partition
		- One of the consumer crashes
	- During this short window of rebalance, consumer cannot consumer messages
	- The consumer loses it's state, so it was caching any data, it needs to refresh it caches thus slowing down application until consumer state sets it up again
- Heartbeat:
	- Consumers maintain membership in a consumer group and ownership of the partitions by sending heartbeats to broker designated as group coordinator	
	- It is send when consumer polls and when it commits record it has consumed
	- Failing to send heartbeat for longer enough, its session will timeout and the group coordinator will consider it dead and trigger a rebalance

- Can subsribe to multiple topics using regex for topic name
- Poll Loop which handles.: coordination, partition rebalances, heartbeats, and dat fetching
- poll()
	- Setting time in poll() : How fast do you want to return control to the thread that does the polling
	- Responsible for finding GroupCoordinator
	- Responsible for joining the CG and receiving partition assignment
	- In case of rebalance trigger, it is handled within the poll loop
	- Heartbeats are sent from poll loop
- One consumer per thread is the rule
- 

Key Params:
- fetch.min.bytes
	- Allows consumer to specifiy the min amount of data it wants to receive from the broker while fetching the records. 
	- Reduces the load on both consumer and broker as they have fewer back and forth messages in cses where not much activity happens on tpoics
	- Set it higher then default if the consumer is using too much CPU or reduce load on broker when we have larger number of consumers

- fetch.max.wait.ms
	- How long to wait for fetch.min.bytes
	- Set this lower vaue if you want to meet SLAs

- max.partition.fetch.bytes
	- Max number of bytes service will return per partition
	- Must be larger than the largest message a broker will accept (max.message.size in broker config)
	- Also keep in mind how time it takes for consumer to process data (as this may impact the session timeout, so consider lowering the value)

- heartbeat.interval.ms (def = 3s)
	Must be lower than session.timeout.ms (< 1/3 of session timeout)

- session.timeout.ms (def = 10s)
	If not heartbeats are received by the broker the expiration of this session timeout, then rebalance triggers 

- auto.offset.reset (def = latest)
	- This property controls the behaviour of the consumer when it starts reading a partition for which it doesn't have a committed offset or is invalid offset. 
	- latest : Lacking an offset, the consumer will start reading from newest record
	- earliest: Lacking an offset, the consumer will read all the data in the partition from the beginning

- enable.auto.commit (def = true)
	- Set it to false if you want to control when the offset are committed

- partition.assigment.strategy
	- Range
	- RoundRobin
	- Implement Custom

- client.id
- max.poll.records
	Max number of records a sinlgle poll()  will return		 	 


Commits & Offset:
- If the committed offset is larger than the offset of the last message the client actually processed, all messages between the last processed offset and the committed offset will be missed by the consumer group

- If the committed offset is smaller than the offset of the last message the client pro‐ cessed, the messages between the last processed offset and the committed offset will be processed twice.

Ways of Committing Offset:
- Automatic Commit
- Commit Current Offset
	- setting auto.commit.offset=false, offsets will only be committed when the application explicitly chooses to do so
- Async Commit
	- One drawback of manual commit is that the application is blocked until the broker responds to the commit request. 
	- This will limit the throughput of the application.
	- Throughput can be improved by committing less frequently, but then we are increas‐ ing the number of potential duplicates that a rebalance will create.


- Exit consumer (since it's a infinite loop) via Consumer Wakeup by calling it from separate thread

Key Design Considerations:
- Generally consumers perform high latency operations (complex calculation, write to DB). Thus sinlge consumers falls behind the data published by consumers, hence adding more consumer is good practice. This calls for creating topics with a large number of partitions.

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
