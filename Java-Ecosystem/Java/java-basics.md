# Key points
- volatile: This makes a java variable to be stored in main memory rather than the CPU cache.
- Future: represents result of async computation. Result can be obtained using method get when the computation is completed, blocking if necessary until it is ready.
- Callable: It is similar to runnable object, but it can return any object and is able to throw exception
- Boxing: Convert primitive type to corresponding reference type
- Unboxing: Convert reference type to corresponding primitive type
- Checked Exception : Comile time 
- Unchecked Exception : Runtime
- JDK, JRE, JVM:
*JDK* : Java Development Kit
	Software Development Environment for developing Java applications and applets
	Comprises:
JRE
Interpreter/Loader
Compiler : Javac
Jar archiver : jar
Documentation Generator : Javadoc
JRE + Development Tool

*JRE* : Java Runtime Environment
	It provides minimum requirements for executing a Java application
	Comprises:
Java virtual Machine
Core classes
Supporting files
JVM + Library classes

*JVM* : Java Virtual Machine
	It is:
Specification
Implementation
Runtime instance

- How many instances of JVM per java application?
Each application will get it’s own JVM instance and each JVM instance will be independent of each other
Common scenario: A single application server such as Glassfish or Tomcat running multiple web apps, thus they share a JVM


## Semaphores
- Used for inter-thread communication
- Use case:lock-permit issuing authority, Parking lot problem, Producer-Consumer
- Can be used to restrict the number of users to a particualr resource or a group of resources
- Unlike locks that allows only one user per resource
- It can restrict any given number of users to a resource
- Semaphore with one permit => Binary Semaphore

```
int NO_OF_PERMITS = 1;
Semaphore sem = new Semaphore(NO_OF_PERMITS);
sem.acquire(); //lock
sem.release(); //unlock
```

- Lock can be similar to a binary semaphore but with certain differences
### Semaphore vs Lock:
- Semaphore doesnot have a notion of owner thread
- Many threads can acquire a permit
- Same thread can acquire the semaphore multiple times
- Binary semaphore (initialized with 1) is not reentrant
- Semaphore can be release by any thread (It can be the thread which has not aquired it)
- If available permits are over and the acquire is called, the thread gets blocked until the release() is called. Thus locks serves better in certain scenarios

# Lambda Expressions
- Anonymous functions
- Can be passed as an args to method
- It can be stored in a variable
- It's not associated with a particular class
- It comprises of:
    - List of params
    - A body
    - return type
    - possible a list of exceptions
- Eg: `(parameters) -> expression` or `(parameters) -> { statements; }`
## Method references
- `(args) -> ClassName.staticMethod(Args)` => `ClassName::staticMethod`
- `(arg0, rest) -> arg0.instanceMethod(rest)` => `ClassName::instanceMethod` where arg0 is of type ClassName
- `(args) -> expr.instanceMethod(args)` => `expr::instanceMethod`

# Functional Interfaces
- It specifies only one abstract method
- This abstract method is also called function descriptor, as it defines the signature of lambda exp
- It can have many default methods though
- Eg: Runnable, Comparator, Callable etc.
- **Lambda expressions let you provide the impl of abstract method and treat the whole expression as an instance of concrete impl of functional interface.**
- Common functional interfaces in Java 8:
    - Predicate<T>
    - Consumer<T>
    - Function<T, R>
    - Supplier<T>
    - UnaryOperator<T>
    - BinaryOperator<T>
    - BiPredicate<L,R>
    - BiConsumer<T,U>
    - BiFunction<T,U,R>
    - Runnable
    - Callable
- Use the primitive variations of the above fuctional interfaces when dealing with primitive values
- None of the above functional interfaces allow for checked exceptions
- @FunctionInterface : Good practice to annotate all the functional interfaces

## Optimizing 
- Reduce application startup time using compile-time code generation in replacement of runtime introspection. 
- Ahead-of-Time compilation of the resulting bytecode to native code reduces startup time, as well as memory consumption.