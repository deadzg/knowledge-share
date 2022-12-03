# Spring Basics

#Dependency Injection
Dependency injection is basically providing the objects that an object needs (its dependencies) instead of having it construct them itself. It's a very useful technique for testing, since it allows dependencies to be mocked or stubbed out.


## What all types of bean scopes is supported by Spring?
- **Singletone**: Scopes a single bean definition to a single object instance per Spring IoC container. Used for stateless beans
obj1 has obj2
obj1:inst1 has obj2:inst1
obj1:inst2 has obj2:inst1
obj1:inst3 has obj2:inst1

- **Prototype**: Scopes a single bean definition to any number of object instances. Used for stateful beans. Spring doesnot manage full lifecycle of the prototype bean. It's the responsiblity of the client to destroy the beans.
obj1 has obj2
obj1:inst1 has obj2:inst1
obj1:inst2 has obj2:inst2
obj1:inst3 has obj2:inst3

- **Request**: Scopes a single bean definition to the lifecycle of a single HTTP request; Only valid in the context of web-aware Spring ApplicationContext

- **Session**: Scopes a single bean definition to the lifecycle of a HTTP session. Only valid in the context of web-aware Spring ApplicationContext

- **Global Session**: Scopes a single bean definition to the lifecycle of a global HTTP session. Typically valid when used in portlet context. Only valid in the context of web-aware Spring ApplicationContext

## What does @SpringBootApplication comprises of?
- @Configuration: Annotated classes with @Configuration will be the candidate for bean definitions and will be bootstrapped by Spring

- @EnableAutoConfiguration: Automatically configures application based on the dependencies added in pom.xml.
Eg: If spring-data-jpa and spring-jdbc is in classpath, then it automatically tries to configure a DataSource by reading database properties from application.properties

- @ComponentScan: It tells Spring to scan and bootstrap other components defined in the current and subpackages

## Spring Boot Notes
- Spring uses Hibernate as the default JPA impl
- @RestController: It's a combination of @Controller and @ResponseBody annotations
- @Controller : Defines a controller
- @ResponseBody: Indicates the return value of a method should be used as the response body for the request
- @RequestMapping: Declares base url for all apis in the controller
- @GetMapping: It's short for RequestMapping with Method type
- @RequestBody: Bind the requestBody with a method param
- @Valid: Makes sure the request body is valid
- @PathVariable: Bind a path variable with method param
- ResponseEntity :is meant to represent the entire HTTP response. You can control anything that goes into it: status code, headers, and body
- @Autowire: It allows Spring to resolve and inject collaborating beans into our bean.
- @Qualifier: If more than one bean of the same type is available in the container, then this annotation is used to specify which bean to pick up during the autowiring
- @ControllerAdvice: It intercepts exceptions from controllers accross the application.

## Configuration
Spring provides various ways to override the default application context properties ie. via:
- Code
- CLI arguments
- Servlet Config Init params
- ServletContext Init params
- Java system properties
- Operating system variables
- application.properties files
*Note*: `application.properties` has the lowest precendence

## Logging
Spring Boot 2.1 onwards supports the logging groups. For this declare the group via `logging.group` configuration property

Then apply the logging level to the group at one shot.

Eg:
Create a logging group dao: `logging.group.dao=com.smalwe.dao, com.smalwe.repo`

Set the log level of group dao to info: `logging.level.dao=DEBUG`

## JPA
- Java Persistence API
- @Entity: Informs JPA that this class and it's objects should 
be persisted

- @Table: Details of the table that this entity will be mapped to

- @Id: Define primary key

- @GeneratedValue: Defines the primary key generation strategy

- @NotBlank: Validate the field is not null

- @Column: Define properties of the column that is mapped to the field. Eg: name, length, nullable, updateable

- @Temporal: Used with java.util.Data and java.util.Calendar classes. It converts data and time values from Java Object to compatible database type and vice versa

- @JsonIgnoreProperties : It's a jackson annotation. Spring boot uses Jackson for serializing and deserializing java objects.
It's used To ignore these properties if provided by client.

- @CreatedData, @LastModifiedDate: These fields will be automatically populated whenever we create or update an entity

- @EntityListeners: It takes the listener class which has jpa lifecycle callback methods. Mostly used for auditing purpose

- @EnableJpaAuditing: Used for enabling the auditing

- JpaRepository<T,ID>: Interface which defines all CRUD operation on an entity with default impl of SimpleJpaRepository. This is plugged by Spring automatically at runtime.
T=> type of entity to handle
ID =>  the type of the entity's identifier

## How to generate Swagger document in Spring Boot Application?
- You need to use SpringFox dependency and provide a Docket bean which is the main bean used to configure SpringFox

## Comparison of JDBC vs JPA
- JDBC: is standard for Database Access and running SQL against it. It is one of the underlying technologies behind most Java database access including JPA(for relational data stores) providers
Disadvantage: You can often have some crappy code where lots of mapping between data sets and objects occur, logic is mixed with in SQL

- JPA: is standard for ORM

	It allows to map object in code to db tables. It can hide SQL from developers so they deal in java classes. It allows to load and save data magically.
	Under the hood most JPA providers use JDBC to read and write from and to DB
	JPA is just a specification, meaning there is no implementation. You can annotate your classes as much as you would like with JPA annotations, however, without an implementation, nothing will happen.

- Spring Data JPA vs Hibernate
	Hibernate is a JPA implementation, while Spring Data JPA is a JPA Data Access Abstraction
	Spring Data JPA is not an implementation or JPA provider, it's just an abstraction used to significantly reduce the amount of boilerplate code required to implement data access layers for various persistence stores
	Hibernate provides a reference implementation of the Java Persistence API that makes it a great choice as an ORM tool with benefits of loose coupling.
	Spring Data JPA always requires the JPA provider such as Hibernate or Eclipse Link.

## Tips
- As of Spring Framework 4.3, Spring does not require the @Autowired anotation if a target bean only defines one constructor.

## Ref
- [1] https://www.callicoder.com/spring-boot-rest-api-tutorial-with-mysql-jpa-hibernate/

- [2] https://stackoverflow.com/questions/11881548/jpa-or-jdbc-how-are-they-different

- [3] https://www.vojtechruzicka.com/documenting-spring-boot-rest-api-swagger-springfox/
- [4] https://www.baeldung.com/spring-cloud-bootstrap-properties
- [5] https://www.baeldung.com/spring-boot-log-groups
- [6] https://www.baeldung.com/spring-autowire

