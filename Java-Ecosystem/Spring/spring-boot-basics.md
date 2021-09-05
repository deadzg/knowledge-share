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

Questions:
What configuration did Spring Boot does on its own?
- For eg: When building an web app, you need to be aware of what all dependencies needs to be included.
Spring boot gives a starter package which includes everything related to the type of Spring Application

Explain in detail @EnableAutoConfiguration?

What is spring-boot-starter-parent?
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

