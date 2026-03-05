# Lesson 02 Notes – Variables, Data Types, and Operators


## Variables in JavaScript
Variables store data that can be used and modified in a program.

### Declaration Keywords
- `let` – value can change
- `const` – value cannot change
- `var` – old method (not recommended)

let score = 10;
const pi = 3.14;


## Data Types

JavaScript supports different data types:

String - "Hello"

Number - 25

Boolean - true / false

Undefined - variable declared but not assigned

Null - empty value

Object - collection of values


let name = "Alex";
let age = 20;
let isActive = true;


## JavaScript Operators
Arithmetic Operators

+  // addition
-  // subtraction
*  // multiplication
/  // division
%  // modulus


## Comparison Operators

==   // equal
===  // strict equal
!=   // not equal
>    // greater than
<    // less than


## Creating Shapes in Canvas

Canvas allows drawing shapes using JavaScript.

# Example: Rectangle

let canvas = document.getElementById("myCanvas");
let ctx = canvas.getContext("2d");

ctx.fillStyle = "blue";
ctx.fillRect(50, 50, 100, 60);


## Introduction to Animation and Timers

Animations are created by updating drawings repeatedly.

Common Timers

setInterval() – repeats after a fixed time

setTimeout() – runs once after a delay

requestAnimationFrame() – smooth animation (recommended)


setInterval(() => {
  console.log("Animating...");
}, 1000);



## Debugging JavaScript

Debugging helps find and fix errors in code.

# Common Debugging Tools

- console.log()

- Browser Developer Tools

- Breakpoints

- Error messages

console.log("Ball X:", x);
console.log("Ball Y:", y);