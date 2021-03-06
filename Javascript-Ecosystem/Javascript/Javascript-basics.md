
# Javascript basics
- Javascript is a scripting/programming language of the web browser.
- On web pages it adds interactivity, from simple animation effects to form validation to full-blown single-page applications.
- JS is both **dynamically typed** (infer variable types at runtime) and **weakly typed**(allow types to be inferred as another type).
- Javascript is single threaded language so it can only execute a single task at a time.
- Is JavaScript an interpreted language or a compiled language? With modern browsers, it depends on the browser engine. A nice introduction on youtube https://www.youtube.com/watch?v=dIu_C5Akino&list=PLv4QGK2Lb0hdE3oVRHFM-OMWtmW3qw8L5&index=1
- Javascript is an implementation of ECMAScript standard. ES6(ECMAScript 2020) is the current version. https://en.wikipedia.org/wiki/ECMAScript

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
- Closure is when a function is able to remember and access its lexical scope even when that function is executing outside its lexical scope.
- Closure is associated with an instance of a function, rather than its single lexical definition.
```
for(var i=0; i<10; i++) {
  (function() {
    var j=i;
    setTimeout(function timer() {
      console.log(j);
    }, j*1000);
  })();
}

for(let i=0; i<10; i++) {  
  setTimeout(function timer() {
    console.log(i);
  }, i*1000);
}
```

### Different coding patterns

#### IIFE (Immediately Invoked Function Expressions)
An IIFE (Immediately Invoked Function Expression) is a JavaScript function that runs as soon as it is defined.
It is a design pattern which is also known as a Self-Executing Anonymous Function and contains two major parts:

- The first is the anonymous function with lexical scope enclosed within the Grouping Operator (). This prevents accessing variables within the IIFE as well as polluting the global scope.
- The second part creates the immediately invoked function expression () through which the JavaScript engine will directly interpret the function.

```
(function() {
...  
}) ()
```

#### Constructor pattern
```
// we define a constructor for Person objects
function Person(name, age, isDeveloper) {
    this.name = name;
    this.age = age;
    this.isDeveloper = isDeveloper || false;

    this.writesCode = function() {
      console.log(this.isDeveloper? "This person does write code" : "This person does not write code");
    }
}

// creates a Person instance with properties name: Bob, age: 38, isDeveloper: true and a method writesCode
var person1 = new Person("Bob", 38, true);
// creates a Person instance with properties name: Alice, age: 32, isDeveloper: false and a method writesCode
var person2 = new Person("Alice", 32);

// prints out: This person does write code
person1.writesCode();
// prints out: this person does not write code
person2.writesCode();
```

- The problem with this approach is that the method writesCode gets redefined for each of the instances of the Person constructor. We can avoid this by setting the method into the function prototype.

#### Prototype pattern
Anything on the prototype is only in memory once.

```
// we define a constructor for Person objects
function Person(name, age, isDeveloper) {
    this.name = name;
    this.age = age;
    this.isDeveloper = isDeveloper || false;
}

// we extend the function's prototype
Person.prototype.writesCode = function() {
    console.log(this.isDeveloper? "This person does write code" : "This person does not write code");
}

// creates a Person instance with properties name: Bob, age: 38, isDeveloper: true and a method writesCode
var person1 = new Person("Bob", 38, true);
// creates a Person instance with properties name: Alice, age: 32, isDeveloper: false and a method writesCode
var person2 = new Person("Alice", 32);

// prints out: This person does write code
person1.writesCode();
// prints out: this person does not write code
person2.writesCode();
```

#### Module Pattern
- It is used to define objects and specify the variables and the functions that can be accessed from outside the scope of the function.
- The most useful thing that this pattern introduces is the clear separation of private and public parts of an object, which is a concept very similar to developers coming from a classical object-oriented background.

```
function jane() {
  const name = 'jane';
  const mid = 'A';
  const final = 'B+';
  return {
    midtermScore: () => mid,
    finaltermScore: () => final,
  }
}
jane().midtermScore(); // A
jane().finaltermScore(); // B+
```

```
/ through the use of a closure we expose an object
// as a public API which manages the private objects array
var collection = (function() {
    // private members
    var objects = [];

    // public members
    return {
        addObject: function(object) {
            objects.push(object);
        },
        removeObject: function(object) {
            var index = objects.indexOf(object);
            if (index >= 0) {
                objects.splice(index, 1);
            }
        },
        getObjects: function() {
            return JSON.parse(JSON.stringify(objects));
        }
    };
})();

collection.addObject("Bob");
collection.addObject("Alice");
collection.addObject("Franck");
// prints ["Bob", "Alice", "Franck"]
console.log(collection.getObjects());
collection.removeObject("Alice");
// prints ["Bob", "Franck"]
console.log(collection.getObjects());
```

#### Revealing Module pattern
```
// we write the entire object logic as private members and
// expose an anonymous object which maps members we wish to reveal
// to their corresponding public members
var namesCollection = (function() {
    // private members
    var objects = [];

    function addObject(object) {
        objects.push(object);
    }

    function removeObject(object) {
        var index = objects.indexOf(object);
        if (index >= 0) {
            objects.splice(index, 1);
        }
    }

    function getObjects() {
        return JSON.parse(JSON.stringify(objects));
    }

    // public members
    return {
        addName: addObject,
        removeName: removeObject,
        getNames: getObjects
    };
})();

namesCollection.addName("Bob");
namesCollection.addName("Alice");
namesCollection.addName("Franck");
// prints ["Bob", "Alice", "Franck"]
console.log(namesCollection.getNames());
namesCollection.removeName("Alice");
// prints ["Bob", "Franck"]
console.log(namesCollection.getNames());
```

#### Using ES6 module with import and export
- You can export any top-level function, class, var, let, or const.
- ES6 modules are automatically strict-mode code, even if you don’t write "use strict"; in them.
- You can use import and export in modules.
- You don’t have to put everything in an IIFE or a callback. Since the code is a module, not a script, all the declarations will be scoped to that module, not globally visible across all scripts and modules.
- When you run a module containing an import declaration, the modules it imports are loaded first, then each module body is executed in a depth-first traversal of the dependency graph, avoiding cycles by skipping anything already executed.
- Reference - https://hacks.mozilla.org/2015/08/es6-in-depth-modules/

```
export function detectCats(canvas, options) {
  var kittydar = new Kittydar(options);
  return kittydar.detectCats(canvas);
}

export class Kittydar {
  ... several methods doing image processing ...
}

// This helper function isn't exported.
function resizeCanvas() {
  ...
}
```
```
import {detectCats, Kittydar} from "kittydar.js";
```

### this binding
- In most cases, the value of this is determined by how a function is called (runtime binding).
- It can't be set by assignment during execution, and it may be different each time the function is called.
- You can use call and apply methods to set the value for this.
- ES5 introduced the bind() method to set the value of a function's this regardless of how it's called.
- ES6(ES2015) introduced arrow functions which don't provide their own this binding (it retains the this value of the enclosing lexical context).

```
// Create obj with a method bar that returns a function that
// returns its this. The returned function is created as
// an arrow function, so its this is permanently bound to the
// this of its enclosing function. The value of bar can be set
// in the call, which in turn sets the value of the
// returned function.
var obj = {
  bar: function() {
    var x = (() => this);
    return x;
  }
};

// Call bar as a method of obj, setting its this to obj
// Assign a reference to the returned function to fn
var fn = obj.bar();

// Call fn without setting this, would normally default
// to the global object or undefined in strict mode
console.log(fn() === obj); // true

// But caution if you reference the method of obj without calling it
var fn2 = obj.bar;
// Calling the arrow function's this from inside the bar method()
// will now return window, because it follows the this from fn2.
console.log(fn2()() == window); // true
```

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this

### AJAX (Asynchronous JavaScript And XML)
- AJAX’s most appealing characteristic is its "asynchronous" nature, which means it can communicate with the server, exchange data, and update the page without having to refresh the page.
- It can send and receive information in various formats, including JSON, XML, HTML, and text files.

Following are the different ways to make asynchronous request:

#### Using XMLHttpRequest object
- Reference - https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest

#### Using promises with XMLHttpRequest object
- A Promise is an object representing the eventual completion or failure of an asynchronous operation.
- Essentially, a promise is a returned object to which you attach callbacks, instead of passing callbacks into a function.
- One of the great things about using promises is chaining.
- Reference - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises

```
let request = obj => {
    return new Promise((resolve, reject) => {
        let xhr = new XMLHttpRequest();
        xhr.open(obj.method || "GET", obj.url);
        if (obj.headers) {
            Object.keys(obj.headers).forEach(key => {
                xhr.setRequestHeader(key, obj.headers[key]);
            });
        }
        xhr.onload = () => {
            if (xhr.status >= 200 && xhr.status < 300) {
                resolve(xhr.response);
            } else {
                reject(xhr.statusText);
            }
        };
        xhr.onerror = () => reject(xhr.statusText);
        xhr.send(obj.body);
    });
};

request({url: "employees.json"})
    .then(data => {
        let employees = JSON.parse(data);
        let html = "";
        employees.forEach(employee => {
            html += `
                <div>
                    <img src='${employee.picture}'/>
                    <div>
                        ${employee.firstName} ${employee.lastName}
                        <p>${employee.phone}</p>
                    </div>
                </div>`;
        });
        document.getElementById("list").innerHTML = html;
    })
    .catch(error => {
        console.log(error);
    });
```
#### Using fetch API
- The Fetch API provides a JavaScript interface for accessing and manipulating parts of the HTTP pipeline, such as requests and responses.
- This kind of functionality was previously achieved using XMLHttpRequest.
- Reference - https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
```
//Say we wanted to fetch a URL and log the response as text. Here's how it looks using promises:
function logFetch(url) {
  return fetch(url)
    .then(response => response.text())
    .then(text => {
      console.log(text);
    }).catch(err => {
      console.error('fetch failed', err);
    });
}
```

#### Using async and await
- Async functions are enabled by default in Chrome 55 and they're quite frankly marvelous. They allow you to write promise-based code as if it were synchronous, but without blocking the main thread. They make your asynchronous code less "clever" and more readable.
- If you use the async keyword before a function definition, you can then use await within the function. When you await a promise, the function is paused in a non-blocking way until the promise settles. If the promise fulfills, you get the value back. If the promise rejects, the rejected value is thrown.
- Reference: https://developers.google.com/web/fundamentals/primers/async-functions

```
async function logFetch(url) {
  try {
    const response = await fetch(url);
    console.log(await response.text());
  }
  catch (err) {
    console.log('fetch failed', err);
  }
}
```

- It's the same number of lines, but all the callbacks are gone. This makes it way easier to read, especially for those less familiar with promises.

### Event Bubbling and Capturing
- **Bubbling** - When an event happens on an element, it first runs the handlers on it, then on its parent, then all the way up on other ancestors.
- Almost all events bubble. For instance, a focus event does not bubble. But still it’s an exception, rather than a rule, most events do bubble.
- The standard DOM Events describes 3 phases of event propagation:
Capturing phase – the event goes down to the element.
Target phase – the event reached the target element.
Bubbling phase – the event bubbles up from the element.
- Reference - https://javascript.info/bubbling-and-capturing

### Event delegation
- Capturing and bubbling allow us to implement one of most powerful event handling patterns called event delegation.
- The idea is that if we have a lot of elements handled in a similar way, then instead of assigning a handler to each of them – we put a single handler on their common ancestor.
- In the handler we get event.target to see where the event actually happened and handle it.
- The HTML structure is flexible, we can add/remove buttons at any time.
- Reference - https://javascript.info/event-delegation

### Event loop

### Webpack and babel
- Reference - https://www.loginradius.com/blog/async/write-a-javascript-library-using-webpack-and-babel/

### Prototype

### Execution Context
- Execution stack, is a stack with a LIFO (Last in, First out) structure, which is used to store all the execution context created during the code execution.
- When the JavaScript engine first encounters your script, it creates a global execution context and pushes it to the current execution stack. Whenever the engine finds a function invocation, it creates a new execution context for that function and pushes it to the top of the stack.
- The engine executes the function whose execution context is at the top of the stack. When this function completes, its execution stack is popped off from the stack, and the control reaches to the context below it in the current stack.
- The execution context is created in two phases: 1) Creation Phase and 2) Execution Phase.
- Refer https://blog.bitsrc.io/understanding-execution-context-and-execution-stack-in-javascript-1c9ea8642dd0#:~:text=Simply%20put%2C%20an%20execution%20context,run%20inside%20an%20execution%20context.


https://jsonplaceholder.typicode.com/todos
