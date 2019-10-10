
# SQS

## Overview

1. It’s a webservice to access the message queue.
2. It’s distributed in nature
3. It’s a pull based system.  For push based you need to use SNS
4. Visibility timeout : The amount of time after which the message is visible again after it’s picked up by a consumer. If consumer processes the message with in this timeout, it will be deleted. If not processed it will be reappear again in the queue. So adjust your timeout accordingly. Default :30secs ; Max is the 12hrs timeout
5. We can configure auto-scaling based on the number of messages in the queue. For eg: If the queue number goes above 10, then provision an additional EC2 instance
6. 256KB in size
7. Messages can be kept in queue from 1 minute to 14 days. Default is 4 days
8. SQS Long polling vs Short Polling: Short polling will keep on pinging the queue for getting msgs even if it is empty, thus cost money as you may end up making requests unnecessarily. Long polling will poll once and then waits for timeout until the next poll is done 


## Types of Queues

### Standard Queue (Default)
1. Unlimited number of transactions. 
2. Message delivered atleast once
3. No order ensured. It tries  to deliver in order

### Fifo Queue (Newly added)
1. Ordered is ensured
2. Message is delivered once and avialable until the consumer deletes it
3. Duplicates are not introduced into the queue
4. It supports message groups
5. 300 transactions per second

## Factors to be Considered
- Pricing
- Limitations
- Monitoring and Logging

## Food For Thought...
Use-cases for SQS
How it is compared to Kafka?
How it is compared to MKS?


