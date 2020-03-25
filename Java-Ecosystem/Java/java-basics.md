# Key points
- volatile: This makes a java variable to be stored in main memory rather than the CPU cache.
- Future: represents result of async computation. Result can be obtained using method get when the computation is completed, blocking if necessary until it is ready.
- Callable: It is similar to runnable object, but it can return any object and is able to throw exception

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
- Can be passed an args to method
- It can be stored in a variable
- It's not associated with a particular class
- It comprises of:
    - List of params
    - A body
    - return type
    - possible a list of exceptions
- Eg: `(parameters) -> expression` or `(parameters) -> { statements; }`

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
- @FunctionInterface : Good practice to annotate all the functional interfaces

