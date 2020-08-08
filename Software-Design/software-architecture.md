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
- Highly Available(HA) : 

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




## Resources 
- https://conferences.oreilly.com/software-architecture
- https://resources.sei.cmu.edu/news-events/events/saturn
- AWS Well Architected Framework : https://d1.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf
- https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/wellarchitected-financial-services-industry-lens.pdf
- TOGAF : https://pubs.opengroup.org/architecture/togaf9-doc/arch/?ref=wellarchitected-wp
- Zackman Framework : https://www.zachman.com/about-the-zachman-framework?ref=wellarchitected-wp
- 