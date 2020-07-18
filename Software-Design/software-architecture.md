# Basics
Core factors to be considered
- Scalability : Ability to scale when the load increases
- Reliability : Ability to prevent and quickly recover from failure
- Security : Protecting information and systems
- Maintainability : Running and monitoring systems
- Testability : 
- Deployability :
- Performance Efficiency : Using IT and computing resources efficiently.
- Cost Optimization : Avoiding unnecessary costs

## Documenting Software Architectures by Bass 
4+1 View Model of Software Architecture
- Logical View
- Implementation View
- Process View
- Deployment View

## Layered Architecture Style
- Presentation Layer
- Business Logic Layer
- Persistence Layer

## Steps
- Define the Domain from the User stores
- Define the System Operations
- Break the system into services by:
	- Business Capility
	- Subdomain
	- SRP
	- CCP
- Hexagonal Architecture

## Issues:
- Network Latency
- Reduced Availability due to sync communication
- Maintaining data consistency across services
- Obtaining a consistent view od data
- God classes preventing decomposition

## Robust RPI Proxies:
- Network timeouts
- Limiting number of outstanding requests from client to a service
- Circuit Breaker Pattern

In such cases prepare for partial failure scenarios:
- Either send an error
- Either send a cached response 




## Architecture Conference 
- https://conferences.oreilly.com/software-architecture
- https://resources.sei.cmu.edu/news-events/events/saturn