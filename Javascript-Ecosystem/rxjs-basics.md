# Reactive Programming Basics
# Observable
- Observables: They are wrapper around a stream of data
- Observer: Observer stares at observables and check for any new value occured/ or error/ or it’s done and thus take the necessary action. You do this using subscription
It has three methods : 
    - next() : Will be called by the observer whenever a new value comes
    - error() : Will be called when an error is thrown by observable
    - complete() : Will be called when the observable is done listening to the stream. Some observables will never finish .For eg: click on button , as the user can click any time

- When does an observer know to call any of the above three methods?
The observable and observer signs a contract using subscribe using which an observable can fire one of these three methods in observer and the observer know one of three methods would be fired by observable and react whenever they are fired

# Subject
- Subject are active event emitters, used when you want to force emit some value from an observable. They are inherited from observable

# References
- [1] https://www.youtube.com/watch?v=Tux1nhBPl_w