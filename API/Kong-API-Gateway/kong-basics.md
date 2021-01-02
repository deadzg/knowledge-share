# Kong Basics
- Kong Gateway exposes the RESTful Admin API on port :8001
- The gateway’s configuration, including adding Services and Routes, is done through requests to the Admin API

## Service
- It is an entity representing an external upstream API or microservice
- Before you can start making requests against the Service, you will need to add a Route to it
- Routes determine how (and if) requests are sent to their Services after they reach Kong Gateway.
- A single Service can have many Routes
- At least one of the hosts, paths, or methods must be set for the route to be matched to the service

## Routes
- Route entities define rules to match client requests
- Each Route is associated with a Service, and a Service may have multiple Routes associated to it
- Every request matching a given Route will be proxied to its associated Service
- 

curl -i -X POST http://localhost:8001/services/smalwe_service/routes \
  --data 'paths[]=/mock, /mock1' \
  --data name=mocking1


## Setup Kong
- https://docs.konghq.com/install/docker/

# References
- Admin API Doc: https://docs.konghq.com/2.0.x/admin-api

