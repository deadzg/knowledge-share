Spring Boot Basics
 - Light-weight framework that takes most of the work out of configuring Spring-based applications.
 - Why Spring Boot: Configuration takes a lot of time in Spring Applications. Thus quickly get a Spring app up and running with very little configuration
 - Spring Boot is opinionated. It has reasonable defaults which can be changed if needed. For eg: Tomcat is very popular web container. By default Spring Boot web application uses an embedded Tomcat container
 - Easily customizable
 - Starters: Used to limit the amount of manual dependency config
 			 It's a set of dependencies that are specific to type of application the starter represents.
 			 spring-boot-starter-xyz
 			 xyz can be: web, jersey, jdbc
 - Auto-configuration: Spring Boot uses its @EnableAutoConfiguration/@SpringBootApplication annotation to automatically configure your application.
 For eg: If you have HSQLDB on your classpath and you have not manually configured any database connection beans, then Spring Boot auto configures an in-memory database.			 
 You can add exclude attribute to disable specific auto configuration
 - Spring Boot uber jar: Spring boot packages the application and its dependencies into a single exe jar

 - Provide a range of non-functional features that are common to large classes of projects (such as embedded servers, security, metrics, health checks, and externalized configuration).



Logging Spring Boot:
- If you use Starters , logback is used for logging

# Questions:
## What configuration did Spring Boot does on its own?
- For eg: When building an web app, you need to be aware of what all dependencies needs to be included.
Spring boot gives a starter package which includes everything related to the type of Spring Application

## Explain in detail @EnableAutoConfiguration?

## What is spring-boot-starter-parent?
 All Spring Boot projects typically use spring-boot-starter as the parent in pom.xml

<parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>1.4.0.RELEASE</version>
</parent>

Parent pom allows to manage following things for multiple child projects:
 - Configuration
 Eg: 
 <java.version>1.6</java.version>
<resource.delimiter>@</resource.delimiter> <!-- delimiter that doesn't clash with Spring ${} placeholders -->
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
<maven.compiler.source>${java.version}</maven.compiler.source>
<maven.compiler.target>${java.version}</maven.compiler.target>

 - Dependency Management : Version of dependencies
Spring boot starter parent inherit from spring boot dependencies. 
Spring Boot Dependencies defines the default dependency management for all Spring Boot projects.
If we would want to use a new version of a specific dependency, we can override the version by specifying a new property in the project pom
Eg:
<properties>
	<activemq.version>5.13.4</activemq.version>
	...
	<ehcache.version>2.10.2.2.21</ehcache.version>
	<ehcache3.version>3.1.1</ehcache3.version>
	...
	<h2.version>1.4.192</h2.version>
	<hamcrest.version>1.3</hamcrest.version>
	<hazelcast.version>3.6.4</hazelcast.version>
	<hibernate.version>5.0.9.Final</hibernate.version>
</properties>


 - Default Plugin Configuration
maven-failsafe-plugin, maven-jar-plugin and maven-surefire-plugin

http://www.springboottutorial.com/spring-boot-starter-parent


- Autoconfiguration of HATEOAS's by using @EnableHypermediaSupport

## Spring Security
- Authentication
- Authorization
- Principal
	Currently logged in user
- Granted Authority
- Roles
	Group of authorities

***Spring Security default behaviour***
- Adds mandatory authentication for URLs
- Adds login form
- Handles login error
- Creates a user (default username:user) and sets a default password
	You can customize the user and password by adding the below properties in application.properties file
	spring.security.user.name=testuser
	spring.security.user.password=pass

AuthenticationManager
authenticate()

AuthenticationManagerBuilder


 -> Manages security in spring app


HttpSecurity let's you configure the paths and the level of access to those paths


How does Spring Security works?
When you inject the spring security dependency it by default intercepts all your request using the concept called Filters

Filter is a contrcut in a servlet application which allows you to intercept the request coming in.
Usually there is a one to one mapping between a url and a servlet method

Filter can be applied to wide range of urls

https://www.youtube.com/watch?v=caCJAJC41Rk&list=PLqq-6Pq4lTTYTEooakHchTGglSvkZAjnE&index=6&ab_channel=JavaBrains

When you inject the Spring security it intercepts /*  ie. all the request to it's own filter DelegatingFilterProxy

DelegatingFilterProxy -> It doesn't do the job itself , but delegates to the respective filters which actually does the job

For authentication you have Auhentication Filter
Same with Authorization filter

When Spring Security authenticates a request it takes input as creds and return principal as output
It keeps track of input and output using an object of type Authentication and once the user is authenticated it stores principal

Providers actually does the authentication
AuthenticationProvider (Interface)
	authenticate() -> Need to implement this


An application can have multiple authentication provider based on number of types of authentication (eg: OAuth2, LDAP, Basic etc.)type the app supports

These different types of authentication type is managed by AuthenticationManager
	authenticate()

ProviderManager implements AuthenticationManager

It delegates the work to the respective AuthenticationProvider


In order for AuthenticationProvider to let ProviderManager know what kind of auth it (AuthenticationProvider) supports  has support() method


In order to implement authentication() of AuthenticationProvider, it needs to load the user details from some identity provider.

For this Spring exposes UserDetailsService loadUserByUsername()
and return the User object

This user object form the Principal which is returned via authenticate  method as Authenticate object

It stores this Authenticate objct containing the Principal in Security Context in ThreadLocal.
The reason which you don't have to login again because it's stored in user session. There is a filter which  manages user session. It takes the authenticated principal and associates it with user session

If the creds are not correct, then a Authentication Exception is thrown which bubbles up till the Autnetication Filter and thrown as an error page or handled based on the logic

This is how you configure the user schema in a database
https://docs.spring.io/spring-security/reference/servlet/appendix/database-schema.html#_user_schema

## Spring Actuator
Actuator is mainly used to expose operational information about the running application — health, metrics, info, dump, env, etc. It uses HTTP endpoints or JMX beans to enable us to interact with it.


References:
[1] https://www.baeldung.com/spring-boot-actuators