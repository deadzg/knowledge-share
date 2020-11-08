# Stream App Properties:
A stream app leverages Consumer and Producer API
- `bootstrap.servers`:
- `auto.offset.reset.config`: set to `earliest` to consume the topic from start
- `application.id`: specific to Streams application, will be used for:
    - Consumern group.id = application.id
    - Default client.id prefix
    - Prefix to internal changelog topics
- default[key|value].serde

## Best Practices
- Always print the topology of the stream using `<streamName>.toString()`
- Close the application gracefully
