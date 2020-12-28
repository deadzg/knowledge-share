
# Javascript basics
- Javascript is a scripting/programming language of the web browser.
- On web pages it adds interactivity, from simple animation effects to form validation to full-blown single-page applications.
- JS is both **dynamically typed** (infer variable types at runtime) and **weakly typed**(allow types to be inferred as another type).
- Javascript is single threaded language so it can only execute a single task at a time.
- Is JavaScript an interpreted language or a compiled language? It depends on the browser engine.

### Data types
Following are the built-in types:

- number
- string
- boolean
- null
- undefined
- symbol (new to ES6)
- object

JavaScript provides a typeof operator that can examine a value and tell you what type it is.

### Global objects
**window**

- A global variable, `window`, represents the window in which the script is running, is exposed to JavaScript code.
- Refer https://www.w3schools.com/jsref/obj_window.asp for window object properties and functions. Alternatively, you could type *window* in the console and you can see the same.
- Any variables and functions defined in this scope are global and accessible everywhere.
- window.document property points to the DOM document loaded in that window. Refer https://www.w3schools.com/jsref/dom_obj_document.asp for the document object properties and functions.

### Variable Hoisting

### Scope ()
- Two types of scope. Global and Local.
- Scope in a programming language controls the visibility and lifetimes of variables and parameters.
- Variables inside the Global scope can be accessed and altered in any other scope.
- All variables defined in a block are not visible from outside of the block.
- Javascript uses Lexical(Static) Scope model.
- Lexical Scope means that in a nested group of functions, the inner functions have access to the variables and other resources of their parent scope. This means that the child functions are lexically bound to the execution context of their parents.
```
function grandfather() {
    var name = 'Hello';
    // likes is not accessible here
    function parent() {
        // name is accessible here
        // likes is not accessible here
        function child() {
            // Innermost level of the scope chain
            // name is also accessible here
            var likes = 'Coding';
        }
    }
}
```
- Before ECMAScript 6, JavaScript only had function scope. Currently, variables declared with "let" and "const" has block scope.

### IIFE

### Closures

### Event loop

### Prototype

### this binding

### Module Pattern

### Execution Context
- Execution stack, is a stack with a LIFO (Last in, First out) structure, which is used to store all the execution context created during the code execution.
- When the JavaScript engine first encounters your script, it creates a global execution context and pushes it to the current execution stack. Whenever the engine finds a function invocation, it creates a new execution context for that function and pushes it to the top of the stack.
- The engine executes the function whose execution context is at the top of the stack. When this function completes, its execution stack is popped off from the stack, and the control reaches to the context below it in the current stack.
- The execution context is created in two phases: 1) Creation Phase and 2) Execution Phase.
- Refer https://blog.bitsrc.io/understanding-execution-context-and-execution-stack-in-javascript-1c9ea8642dd0#:~:text=Simply%20put%2C%20an%20execution%20context,run%20inside%20an%20execution%20context.
