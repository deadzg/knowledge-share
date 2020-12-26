#GraalVM

## What is GraalVM

## Benefits
- Java applications can run with fast execution and low memory footprint using GraalVM Ahead of Time compilation(AOT). Good for microservices and serverless usecases
- Polyglot Capability: It can run code in several languages ie. It enables a code to run in one language to interoperate with code in another language

## Comparing Memory Footprint
### Setup
- Comparison is done using Java11 with GraalVM and AdoptOpenJDK
- Switch to AdoptOpenJDK: `jdk 11.0.7`
- Switch to GraalVM: `jdk 11`
- Run a Java application
- Grep the pid for the application: `ps -efx | grep java`
- Get memory footprint: `jstat -gc <pid>`

## Key Concepts
- `JIT compiler`:  Converts bytecode to executable machine code
    - A JIT compiler runs after the program has started and compiles the code (usually bytecode or some kind of VM instructions) on the fly (or just-in-time, as it's called) into a form that's usually faster, typically the host CPU's native instruction set. A JIT has access to dynamic runtime information whereas a standard compiler doesn't and can make better optimizations like inlining functions that are used frequently.

    This is in contrast to a traditional compiler that compiles all the code to machine language before the program is first run.

- `AOT compiler`:
    While JIT technique enables the JVM to produce highly optimized code and improves peak performance, the startup time is likely not optimal, as the executed code is not yet JIT compiled. AOT aims to improve this so-called warming-up period

    AOT compilation is one way of improving the performance of Java programs and in particular the startup time of the JVM

## Hands-On
- JIT for Java
- AOT for Java
- Polyglot Runtime for Node, JS, Python, R, Ruby
- Java interoperability to JavaScript, Python
- Interoperability from Node/JavaScript, Python and other languages to Java
- Multi directional polyglot interoperability

## References
- [1] https://medium.com/oracledevs/quickest-route-to-your-first-handson-experience-with-graalvm-katacoda-scenario-with-live-2dd5489b92e0
- [2] https://stackoverflow.com/questions/95635/what-does-a-just-in-time-jit-compiler-do