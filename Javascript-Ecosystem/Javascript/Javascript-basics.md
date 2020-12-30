
# Javascript basics
- Javascript is a scripting/programming language of the web browser.
- On web pages it adds interactivity, from simple animation effects to form validation to full-blown single-page applications.
- JS is both **dynamically typed** (infer variable types at runtime) and **weakly typed**(allow types to be inferred as another type).
- Javascript is single threaded language so it can only execute a single task at a time.
- Is JavaScript an interpreted language or a compiled language? With modern browsers, it depends on the browser engine. A nice introduction on youtube https://www.youtube.com/watch?v=dIu_C5Akino&list=PLv4QGK2Lb0hdE3oVRHFM-OMWtmW3qw8L5&index=1
- Javascript is an implementation of ECMAScript standard. ES6(ECMAScript 2015) is the current version.

### Data types
Following are the primitive types:

- number
- string
- boolean
- null
- undefined
- object
- symbol (new to ES6)

Rest everything are objects. Eg. array, function...

JavaScript provides a typeof operator that can examine a value and tell you what type it is.
```
var a;
typeof a;				// "undefined"

a = "hello world";
typeof a;				// "string"

a = 42;
typeof a;				// "number"

a = true;
typeof a;				// "boolean"

a = null;
typeof a;				// "object" -- weird, bug

a = undefined;
typeof a;				// "undefined"

a = { b: "c" };
typeof a;				// "object"
```

### Objects
```
var obj = {
	a: "hello world",
	b: 42,
	c: true
};

obj.a;		// "hello world"
obj.b;		// 42
obj.c;		// true

var d = "a";

obj["a"];	// "hello world"
obj["b"];	// 42
obj["c"];	// true
obj[d]; // "hello world"
```
- Properties can either be accessed with dot notation (i.e., obj.a) or bracket notation (i.e., obj["a"]). Dot notation is shorter and generally easier to read, and is thus preferred when possible.
- Bracket notation is useful if you have a property name that has special characters in it, like obj["hello world!"] or if you want to access a property/key but the name is stored in another variable.

### Arrays
```
var arr = [
	"hello world",
	42,
	true
];

arr[0];			// "hello world"
arr[1];			// 42
arr[2];			// true
arr.length;		// 3

typeof arr;		// "object"
```
- An array is an object subtype that holds values (of any type) not particularly in named properties/keys, but rather in numerically indexed positions.

### Function
Javascript functions are first class objects. Which means they can be:
- stored in a variable, object, or array.
- passed as an argument to a function.
- returned from a function.
```
//Function declaration syntax
function foo() {
	return function bar() {}
}

//Anonymous function expression
var foo = function() {
	// ..
};

//Named function expression
var x = function bar(){
	// ..
};
```
Though it may not seem obvious from the first syntax, foo is basically just a variable in the outer enclosing scope that's given a reference to the function being declared. That is, the function itself is a value.

### Global objects
**window**

- A global variable, `window`, represents the window in which the script is running, is exposed to JavaScript code.
- Refer https://developer.mozilla.org/en-US/docs/Web/API/Window for window object properties and functions. Alternatively, you could type *window* in the console and you can see the same.
- Any variables and functions defined in this scope are global and accessible everywhere.
- window.document property points to the DOM document loaded in that window. Refer https://developer.mozilla.org/en-US/docs/Web/API/Window/document for the document object properties and functions.

### Scope
- Two types of scope. Global and Local.
- Scope in a programming language controls the visibility and lifetimes of variables and parameters.
- Variables inside the Global scope can be accessed and altered in any other scope.
- All variables defined in a block are not visible from outside of the block.
- Javascript uses Lexical(Static) Scope model.
- Lexical Scope means that in a nested group of functions, the inner functions have access to the variables and other resources of their parent scope.
```
function myadd() {
  var a = 1;
  var b = 2;

  function add() {
    return a + b;
  }

  return add;
}

var add = myadd();
console.log(add());
```
- Before ECMAScript 6, JavaScript only had function scope. Currently, variables declared with "let" and "const" has block scope.

### IIFE (Immediately Invoked Function Expressions)
An IIFE (Immediately Invoked Function Expression) is a JavaScript function that runs as soon as it is defined.
It is a design pattern which is also known as a Self-Executing Anonymous Function and contains two major parts:

- The first is the anonymous function with lexical scope enclosed within the Grouping Operator (). This prevents accessing variables within the IIFE as well as polluting the global scope.
- The second part creates the immediately invoked function expression () through which the JavaScript engine will directly interpret the function.

```
```

### Hoisting
Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their scope before code execution.
```
var a = 2;
foo();			// works because `foo()` declaration is "hoisted"

function foo() {
	a = 3;
  console.log( a );	// 3
  var a;				// declaration is "hoisted" to the top of `foo()`
}

console.log(a);
```
- Only declarations are hoisted, now the assignment.
- Variables declared with "var" are moved to the top of its enclosing scope and initialized as "undefined".
- Variables declared with "let" and "const" are moved to the top of its enclosing scope but are now initialized.

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

### AJAX
https://jsonplaceholder.typicode.com/todos
