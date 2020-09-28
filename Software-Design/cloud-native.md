# Cloud Native
Cloud-native technologies empower organizations to build and run scalable applications in modern, dynamic environments such as public, private, and hybrid clouds. Containers, service meshes, microservices, immutable infrastructure, and declarative APIs exemplify this approach

These techniques enable loosely coupled systems that are resilient, manageable, and observable. Combined with robust automation, they allow engineers to make high-impact changes frequently and predictably with minimal toil.

## Twelve Factor Apps
### Codebase
- Source code in version control
- One code repo per microservice
- Multiple env(test, stage, prod..) deployment from same repository

### Dependencies
- Microservice should explicitly declare and isolate dependencies (Use Gradle, Maven etc.)
- It should not rely on system-wide dependencies

### Configuration
- Decouple environment specific settings from the code to configuration
- Never commit any credentials into source repositories

### Backing Services
- Any kind of service the microservice consumes
- Eg: Database, LDAP, Cache, External Service endpoint
- Backing service should be treated as attachable resource

### Build, release, run
- Strictly separate build, release and run stages
- Build stage: Converts code repo into executable bundle known as build
- Release stage: Takes the build produced and combines it with deploy's current config
- Run stage: Runs the app in the execution env by launching some set of apps processes against a selected release

### Processes
- Processes should be stateless ie. microservice should not assume any data to be in memory before or after it executes an operation
- Should avoid using sticky sessions
- Should follow shared nothing architecture ie. a node in the given system should not share either the disk or the memory with other nodes

### Port binding
- Export services via port binding
- Microservice itself has to do port binding and expose it as a service (Eg: Deploying a SpringBoot app complies with this factor)
- Microservice should not rely on runtime injection of a webserver into the execution env to create a web-facing service (Eg: Deploying a WAR in Tomcat doesnot follow this factor)
- A microservice shold be self-contained, self executable JAR files (in case of Java)

### Concurrency
- Microservice should be able to horizontally scale in or scale out

### Disposability
- Microservice should be able to spin up fast (milliseconds) and shutdown gracefully when required
- One microservice per container

### Dev/prod parity
- Ensure the dev, staging and prod env stay identical as much as possible

### Logs
- Treat logs as event streams
- Logs help identify any issues in the system and can be used as audit trail
- Ability to trace and correlate a given request between all the microservices in the system

### Admin Processes
- One-off admin processes should be run in an identical env as the regular long-running processes of the microservice
- Admin code much ship with the application code to avoid synchronization issues
- Eg of an admin task: Running database migration

### Other factors not part of twelve factor
- API First
- Telemetry
- Authn/Authz

## References
- https://docs.microsoft.com/en-us/dotnet/architecture/cloud-native/definition
- https://12factor.net/

