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
