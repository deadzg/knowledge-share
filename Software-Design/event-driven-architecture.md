# Key Terminologies
- Command
- Queries
- Events
- Event Collaboration Pattern
- Event Sourcing
- Command Sourcing
- CQRS
- Exactly Once Processing
- Idempotency
- Log Compaction
- Choreographies
- Rewind & Replay

# Key Principles
- No service knows the existence of another service
- No service owns the entire workflow
- 

## Choreographies
Each service handles some subset of state transitions, which when put together describe the whole business process

## Event Sourcing
- It is the observation that events (state changes) are a core element of any system.
- They are stored, immutably, in order they were created in, resulting event log provides a comprehensive audit of exactly what the system did.

### Advantage of Event Sourcing
- Version control of data
- Store an ordered journal of state changes which is useful for debugging and traceability purposes
- It ensures every state change in a system is recorded
- Events are the source of truth not the db record
- Events are first-class entities
- Solves the data-divergence problem