-  Java Profiler: It's a tool that monitors Java bytecode constructs and operations at JVM Level
- Eg: JProfiler , Java VisualVM, YourKit, JFR 

Before moving into JProfiler it's important to understand how is the code compiled and run in Java
Post compilation of the code (eg: Main.java) the code is converted into bytecode(eg: Main.class)
This bytecode is taken by the JVM and interpreted by each machine's(Mac/Win/Linux) JVM implementation

There are different types of JVM implementation available out in the market. The default one is HotSpot JVM..

JIT compilation makes the process faster by converting certain pieces of code into native machine code based on it's frequency of usage. 
While doing performance analysis for certain functions it's important to understand the analysis is done after the coversion into native code or before the conversion.

To get a view on how the code is running and which pieces are converted into native code we can use the below VM arg while running the application: `-XX:+PrintCompilation`
-XX(Case Sensitive) -> Advanced options
+ -> Switch ON
- -> Switch OFF
```
     45    8       3       java.lang.StringLatin1::indexOfChar (33 bytes)
     72    9       3       java.util.concurrent.ConcurrentHashMap::tabAt (22 bytes)
     73   10       3       jdk.internal.misc.Unsafe::getReferenceAcquire (7 bytes)
     73   11     n 0       java.lang.System::arraycopy (native)   (static)
     73   12       3       sun.nio.fs.UnixPath::checkNotNul (16 bytes)
     73   13       3       java.lang.StringLatin1::canEncode (13 bytes)
     73   14       3       java.util.zip.ZipUtils::SH (21 bytes)
     75   15       1       java.util.zip.ZipCoder$UTF8ZipCoder::isUTF8 (2 bytes)
     75   16   !   3       java.util.zip.ZipFile$Source::checkUTF8 (43 bytes)
     75   17       3       java.util.zip.ZipCoder$UTF8ZipCoder::normalizedHash (90 bytes)
```
First column: Number of milliseconds from the point when virtual machine started
Second column: Order in which the method was compiled
Third column: 
- contains :0,1,2,3,4 
- 0: No compilation ie. the code has just been interpreted
- 1 to 4: Progressivley deeper level of compilation

! :   Method has exception handlers
% :   On stack replacement ie. method has been natively compiled and running in code cache ie. code runnning in most optimal way possible
* :   Generating a native wrapper
s :   Synchronized method
b :   Blocking compiler (always set for client)
n :   Native method
`made not entrant` : compilation was wrong/incomplete, no future callers will use this version
`made zombie` : code is not in use and ready for GC

Two compilers are built into JVM:
- C1: Able to do first three level of compilation. Each level is progressievly more complex than the last one
- C2 : Can do the 4th level. If the code is called too many times we reach C4 level of compilation. Most optimized. Then the code is is put by JVM in **code cache** ie. the special aread of memory for the code to be accessed quickly

- Higher the level of compilation the more optimized the code should be
- JVM doesnot optimize each piece of code into L4 as there is a trade off and benefits are far less.

For application running on remote machines we may not have access to the console. For such scenario's we can log the compilation using:
`-XX:+UnlockDiagnosticVMOptions -XX:+LogCompilation`
Post enabling the option, you will see a log file in the root directory of theh project. Eg: `hotspot_pid77745.log`


Codecache has limited size.Look out for warning: `VM Warning: CodeCache is full. Compiler has been disabled`
This means all the code in the code cache is actively being used. Thus no part of the code cache can be easiliy cleaned up.This means the application is not running in an optimal manner and their is a room for improvement. We can increase the size of the codecache  to improve the performance.
Use the VM option to check the codecache size: `-XX:+PrintCodeCache`
Codecache can be upto 240MB
InitialCodeCacheSize: Codecache size at the start of the application . Generally 160KB
ReservedCodeCacheSize: Maximum size of the codecache
CodeCacheExpansionSize: How quickly the codecache could grow
Eg: Setting the reserved code size to 28 MB. Note: There is no + sign as here we are setting a value of the VM options rather than switching on or off a flag
`-XX:ReservedCodeCacheSize=28m`
As of java9 the codecache is divided into three segements:
- The non-method segment contains JVM internal related code `XX:NonNMethodCodeHeapSize`
- The profiled-code segment contains lightly optimized code with potentially short lifetimes `XX:ProfiledCodeHeapSize`
- The non-profiled segment contains fully optimized code with potentially long lifetimes `XX:NonProfiledCodeHeapSize`

JConsole can be used to monitor the codecache of the application running on a remote machine.
JConsle will intereact with JVM to fetch the metrics and during this process uses around 2MB of codecache.


=======

List of the java process id: `jps`
List of the default Java Flags: `java -XX:+PrintFlagsFinal`
Alternative way to list a given Flag (eg:CICompilerCount): `jinfo -flag CICompilerCount <java-pid>`

Another factor which can impact the application performace is:
- How many threads are available for the JIT compilation process
    - Default number of threads depends on number of CPUs on computer. Check the default threads using: `java -XX:+PrintFlagsFinal | grep CICompilerCount`
    - This number can be increased using the VM option: `-XX:CICompilerCount=n` eg: `-XX:CICompilerCount=6`
- What's the threshold for native compilation i.e.  how many times a method needs to be run before java decides it to convert into native code 
    - `-XX:CompileThreshold=n`
    - Reduce the threshold to improve the performance
Tuning the flags needs some experimentation with the Java application.

Java Memory:
- Stack
    - Every thread will have it's own stack
    - Local variables are stored on the stack
    - It stores values for primitive data types (eg: int, double, float, etc..)
    - Local variables reference the object created in heap
    - All data in a Java application is accessed by a stack
- Heap
    - This stores object
    - String pool lives in Heap. This means the String can be garbage collected
    - intern will put the calculated string in string pool eg: i.toString().intern(). This will minimize the number of object created but it will get an overhead of calling another method ie. intern
    - 

- Metaspace
    - Stores metadata
    - Information about classes, methods eg: Which method are compiled into byte code, which would be compiled in native code
    - Consider it as stack for static variables
    - Primitive static variables are stored in metaspace
    - Static objects are stored on the heap with the object pointer held in metaspace
    - Variables in the metaspace are permanently there
    - Any object in the heap which are referenced from the heap are never be garbage collected
    - All classes and threads within a Java application have access to the Metaspace


- Java is always passing by value
- Passing by reference is not supported in Java
- Generally Heap is huge as compared to Metaspace and Stack

String Pool:
- Implemented using HashMap
- -XX:+PrintStringTableStatistics

Garbage Collection:
- Mark and Sweep
    - Pause (Stop the world event) ie. all threads in the application are paused
    - It looks for every variable in the stack and on the metaspace and the object referenced and mark them as alive
    - Removes all the objects which are not marked
    - Moves the objects into contiguous block of memory to avoid fragmentation
    - Garbage collection actually collects all the objects which are not garbage
- Generation garbage collection
    - With the stop the world event the application might freeze for few seconds. This may be not exceptable by business. Thus we have generational garbage collection.
        - Most objects don't live for long
        - If an object survives for one garbage collection it is likely to live forever
        - It's faster to run garbage collection when there is lot of garbage ie. less number of objects to be marked. The heap is organized into spearate sections(young generation and old generation). This is called the generational garbage collection. 
        - Young gen: 
            - New objects are created in this section. 
            - It's small as compare to old gen, thus gc takes place when it is full but only on young gc (minor gc)
            - It takes fractions of a second
            - No application freeze is noticable
            - Any surviving objects are moved to the old 
            - Young gen becomes empty after every minor gc
        
        - Old gen:
            - Gc runs only when it is full (major gc). Thus frequency of major gc is less than minor gc
            - Takes longer time as there are many objects which are still alive thus these needs to be marked and then compacted into contiguous block of memory
            - This takes upto few seconds, so it might have noticeable impact
[36.299s][info][gc] GC(1750) Pause Young (Normal) (G1 Evacuation Pause) 6M->2M(10M) 0.233ms
    6M -> Heap size before the garbage collection ran
    2M -> Heap size after the garbage collection ran
    0.233ms -> Time taken to run the gc
-Xmx10m -verbose:gc

Use `jps` command to list Java process running in your machine
Check if adaptive policy is on: `jinfo -flag UseAdaptiveSizePolicy 23140`

Tuning GC:
- -XX:-UseAdaptiveSizePolicy
- -XX:NewRatio=n How many times should be the old gen biggers than the young gen
    Eg: -XX:NewRation=4   => Old gen is 4 times bigger than the young gen. So if the heap id of 10 MB, then 8 MB will be Old gen and 2 MB will be new gen
    Find the default value using: `jinfo -flag NewRatio 23140` -> 2
- -XX:SurvivorRation=n => How much of the young gen should be taken by the survivor S0 and S1 and the rest of it would be eden
    Find the default value using: `jinfo -flag NewRatio 23140` -> 8 

- -XX:MaxTenuringThreshold=n => How many generations do object survive before it becomes part of old generation. This number is upper bound. JVM may still choose anything less than that if it thinks it is beneficial for the app performance. `jinfo -flag MaxTenuringThreshold 92305` -> 6

- Selecting a GC
    - Serial: `-XX:+UseSerialGC`
    - Parallel: Multiple threads performing the GC. Good for larger datasets. `-XX:+UseParallelGC`
    - Mostly Concurrent: Applications pause is minimized
        `-XX:+UseConcMarkSweepGC`
        `-XX:+UseG1GC` -> Default Garbage Collector
    
- Tuning G1:
    - `-XX:ConcGCThreads=n` -> Useful when we want to limit the GC threads to lower the impact on other applications
    - `-XX:InitiatingHeapOccupancyPercent=n` -> The G1 starts when heap reaches certain level of occupancy. Default value to 45%
    - `-XX:UseStringDeDepulication` -> Allows the garbage collector to have more space if it find duplicate string in the heap

## References
- https://www.baeldung.com/java-profilers
- JProfiler download : https://www.ej-technologies.com/download/jprofiler/files
- PrintCompilation : https://blog.joda.org/2011/08/printcompilation-jvm-flag.html
- CodeCache: https://docs.oracle.com/javase/8/embedded/develop-apps-platforms/codecache.htm
- https://www.baeldung.com/jvm-code-cache
