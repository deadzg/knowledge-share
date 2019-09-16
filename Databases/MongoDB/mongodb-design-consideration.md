# Data Model Design Consideration

## Questions
- Which version of Mongo are we using?
- What are different data retrival patterns?
- Is JSON Schema Validation required/done?
- Is expression based validation required/done?
- How to handle invalid documents?
- Which data model are we following (Normalized or Denormalized)?
- Are we following a multi-tenant model?If yes what are the defining fields (ie. customer_id or similar fields)
- Are we updating multiple documents in one transaction? If yes how are we handling the atomicity? FYI: In version 4.0 and 4.2 multi-document atomicity is supported
- What is the Shard Key used and why?
- How are indexes created and based on what criteria?
- Do we have multikey indexes?
- Do we have a need for composite indexes?

- How is the capacity planning done?

## Notes
- MongoDB allows related data to be embedded within a single document.
- To join collections(relevant for normalized data), MongoDB provides the aggregation stages: $lookup and $graphlookup
- A write operation is atomic on the level of a single document
- When a single write operation modifies multiple documents, the modification of each document is atomic, but the operation as a whole is not atomic.
- Multi-document transaction incurs a greater performance cost over single document writes
- The availability of multi-document transactions should not be a replacement for effective schema design
- Distinct collections are very important for high-throughput batch processing
- MongoDB always indexes the _id field
- supports indexes on any field or sub-field of the documents
- Single Field Index
- Composite Indexes
- Multikey indexes
- Covered Queries using Projection

## References
https://docs.mongodb.com/manual/core/schema-validation/
https://docs.mongodb.com/manual/core/data-modeling-introduction/

