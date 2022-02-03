# Key points
- Java is `pass-by-value`

    ```java
        public void m1() {
            int x; int y;
            x=5; y=10;
            int r1 = sum (x,y);
            List<Integer> things = new ArrayList<>();
            things.add(x);things.add(y);
            int r2 = sizeOfThings(things); 
        }
        // Primitive values are passed
        public int sum(int x, int y) {
            return x+y;
        }

        // Reference of `things` is passed as the value
        public int sizeOfThings(List<Integer> things) {
            return things.size();
        }
    ```


- Access modifiers: `private` , `public`, `protected`, `default`
- Other modifiers: `static`, `final`, `abstract`, `synchronized`, `volatile`

- `static`: It can be applied to fields and methods. Static fields and methods are class members (NOT object members)

- `final`: Can be used at field, method, class
    - If used with **field** implies the field reference cannot be changed
    - If used with **method** or **class** implies that method or class cannot be extended or overridden
- `abstract`: Implies a class cannot be instantiated. It is meant to only be sub-classed
- `synchronized`: Can be used at instance as well as with static methods and code blocks. It implies we make Java use a monitor lock to provide synchronization for a given code fragment

-  `volatile`: This makes a java variable to be stored or read from  main memory rather bypassing the CPU cache.

-  `Future`: represents result of async computation. Result can be obtained using method get when the computation is completed, blocking if necessary until it is ready.

-  `Callable`: It is similar to runnable object, but it can return any object and is able to throw exception

-  `Boxing`: Convert primitive type to corresponding reference type

-  `Unboxing`: Convert reference type to corresponding primitive type

-  `Checked Exception` : Compile time

-  `Unchecked Exception` : Runtime

- `try-with-resources`: The try-with-resources statement is a try statement that declares one or more resources. A resource is an object that must be closed after the program is finished with it. The try-with-resources statement ensures that each resource is closed at the end of the statement. Any object that implements java.lang.AutoCloseable, which includes all objects which implement java.io.Closeable, can be used as a resource. 

- `shallow copy`: New copy of the object is created but the object contained inside the main object points to the older reference. This means any change in the contaning object will change the cloned object.
  
## Java Memory
- `Heap`: All the objects are created on heap. JVM throws OOM erro when heap is full. String pool is part of Java Heap
- `Stack`: JVM reserves blockes for local variables and additional data. LIFO structure. Whenever a method is called, a new block is reserved for local variables and object references.When method finishes the blocks are released. Stack has much less memory space than heap. It throws StackOverflow error when full (in case of bad recursive call or very deep recursion).

## JDK, JRE, JVM:

***JDK*** : Java Development Kit
 - Software Development Environment for developing Java applications and applets
 - Comprises:
	
	 - JRE
	 - Interpreter/Loader
     - Compiler : Javac
     - Jar archiver : jar
     - Documentation Generator : Javadoc
     - JRE + Development Tool

***JRE*** : Java Runtime Environment
- It provides minimum requirements for executing a Java application
- Comprises:
	- Java virtual Machine
	- Core classes
	- Supporting files
	- JVM + Library classes

***JVM*** : Java Virtual Machine
- It is a virtual machine. Like a real machine, it has an instruction set, a virtual computer architecture and an execution model. It is capable of running code written with this virtual instruction set, pretty much like a real machine can run machine code.[1]

- It comprises of:
    - Specification
    - Implementation
    - Runtime instance

*How many instances of JVM per java application?*

Each application will get it’s own JVM instance and each JVM instance will be independent of each other

Common scenario: A single application server such as Glassfish or Tomcat running multiple web apps, thus they share a JVM

***HotSpot*** : Implementation of JVM concept developed by Sun owned by Oracle now. Other similar implementations of JVM are JRockit, IBM J9 etc.

***OpenJDM*** : It is a project underwhich an opensource implementation of HotSpot is developed 

***JIT compiler***:  Converts bytecode to executable machine code
    - A JIT compiler runs after the program has started and compiles the code (usually bytecode or some kind of VM instructions) on the fly (or just-in-time, as it's called) into a form that's usually faster, typically the host CPU's native instruction set. A JIT has access to dynamic runtime information whereas a standard compiler doesn't and can make better optimizations like inlining functions that are used frequently.

    This is in contrast to a traditional compiler that compiles all the code to machine language before the program is first run.

*** Is Java Compiled or Interpreted ? ***
- Java is a compiled programming language, but rather than compile straight to executable machine code, it compiles to an intermediate binary form called JVM byte code. The byte code is then compiled and/or interpreted to run the program. 
- JVM acts as both interpreter and compiler for converting the bytecode into native code

*** Advantage of JIT Compiler over interpreter ***
- Byte code of a program may usually consist of methods, variables, threads and other instructions.  So, here instead of invoking a method every time the code is interpreted an optimized code is generated by the JIT for a particular machine.
- JIT compiles the code when it is needed but not before runtime. Whenever a program is executed this compiled object code is invoked instead of interpreting the entire byte code and is quite efficient. This increases the performance of the program as well. Just in time compiler coverts the byte code to a platform specific executable code that can be executed immediately. However the use of JIT is optional, but Sun Microsystems suggest that it is quite efficient to use JIT especially if there exists a repeated code in the program.

*** Advantage of AOT over JIT ***
- Compile Java classes to native code prior to launching the virtual machine.
- Improve the start-up time of both small and large Java applications, with at most a limited impact on peak performance.
- JIT compilers are fast, but Java programs can become so large that it takes a long time for the JIT to warm up completely. Infrequently-used Java methods might never be compiled at all, potentially incurring a performance penalty due to repeated interpreted invocations 

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

# Remainder Operator (%)
In Java `%` is the remainder operator unlike in Python which is a modulo operator
Key difference: Modulus is always the same sign as the divisor and remainder the same sign as the quotient.
Eg:
Remainder -> -3 % 2 = -1
Modulus   -> -3 % 2 = 1

For using Modulus in Java: `Math.floorMod(-3,2)`

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

-  `(args) -> ClassName.staticMethod(Args)` => `ClassName::staticMethod`

-  `(arg0, rest) -> arg0.instanceMethod(rest)` => `ClassName::instanceMethod` where arg0 is of type ClassName

-  `(args) -> expr.instanceMethod(args)` => `expr::instanceMethod`

  

# Functional Interfaces

- It specifies only one abstract method

- This abstract method is also called function descriptor, as it defines the signature of lambda exp

- It can have many default methods though

- Eg: Runnable, Comparator, Callable etc.

-  **Lambda expressions let you provide the impl of abstract method and treat the whole expression as an instance of concrete impl of functional interface.**

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

## What is Servlet? [7]
Servlets are the Java programs that run on the Java-enabled web server or application server. They are used to handle the request obtained from the webserver, process the request, produce the response, then send a response back to the webserver. 
Execution of Servlets basically involves six basic steps: 

- The clients send the request to the webserver.
- The web server receives the request.
- The web server passes the request to the corresponding servlet.
- The servlet processes the request and generates the response in the form of output.
- The servlet sends the response back to the webserver.
- The web server sends the response back to the client and the client browser displays it on the screen.

Servelts are maped to a url/endpoint.


## What is Java Servlet Filter?
Java Servlet Filter is used to intercept the client request and do some pre-processing. It can also intercept the response and do post-processing before sending to the client in web application

# References
- [1] https://stackoverflow.com/questions/16568253/difference-between-jvm-and-hotspot
- [2] https://stackoverflow.com/questions/1326071/is-java-a-compiled-or-an-interpreted-programming-language
- [3] https://www.whizlabs.com/blog/what-is-just-in-time-compiler-difference-between-compiler-and-interpreter/
- [4] https://metebalci.com/blog/demystifying-the-jvm-interpretation-jit-and-aot-compilation/
-[5] http://openjdk.java.net/jeps/295
-[6] https://www.baeldung.com/java-interview-questions
-[7] https://www.geeksforgeeks.org/introduction-java-servlets/