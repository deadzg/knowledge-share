https://www.confluent.io/blog/schemas-contracts-compatibility/

https://www.confluent.io/blog/event-sourcing-vs-derivative-event-sourcing-explained/



Design a generic event for Kafka is the key for an enterprise to process the data and make more sense out of it without reprocessing the events/unnecessary ETL pipelines.
Proposed event schema design:

Event Key Design is the key for how the events are distributed across the partitions for a given topic.
Please consider the ordering factor if the  multiple types of events are published in a single topic.

Note the below schema may change based on the product requirements:

Key Schema:
correlationId : This field will help create a relationship between all events in the process. Eg: b04e9ff4-7429-11eb-9439-0242ac130002
processId: The system which generated the event Eg: DigitalGateway, TTC, RegChecker
eventType: Describes the event type. Eg: risk.validation-initiated


Value Schema:

Note the key schema is only for determining the partition of the event. The actual event data is present in the value schema
eventId: Unique identifier for an event
createdAt: 
source.type:
source.id:
attributes : Flexible data structure for any type of metadata to be added in future
contentType: Type of data Eg: application/json
payload: Actual event payload which depends on the type of event