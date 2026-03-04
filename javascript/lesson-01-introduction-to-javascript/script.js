// Selecting Elements
//Get by ID
let title = document.getElementById("demo");
console.log(title);
//Get by class
let items = document.getElementsByClassName("text");
console.log(items);
let item1 = document.getElementsByClassName("text")[1];
console.log(item1);
//Get by tag
let tags = document.getElementsByTagName("p");
console.log(tags);
let tag1 = document.getElementsByTagName("p")[0];
console.log(tag1);

//Modern way- query selectors
let heading = document.querySelector("h3");
console.log(heading);
let allItems = document.querySelectorAll(".food");
console.log(allItems);


// Accessing Object Attributes
//Changing content
let x = document.getElementById("content");
x.textContent = "I love Javascript"; //change text
let y = document.getElementById("inner");
y.innerHTML = "<b>Welcome</b>"; //adds HTML

//Changing Style
x.style.color = "blue";
y.style.fontSize = "15px";

//Creating and Adding Elements
let newPara = document.createElement("p");
newPara.textContent = "New paragraph";
document.body.appendChild(newPara);

let div = document.createElement("div");
let h1 = document.createElement("h1");
let text = document.createTextNode("Hello JavaScript Class");
h1.appendChild(text);
h1.setAttribute("class", "heading");
div.appendChild(h1);
document.body.appendChild(div);
h1.style.color = "red";




//Canvas Coordinate System

const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

// Rectangle
ctx.fillStyle = "blue";
ctx.fillRect(50, 50, 150, 100);

// Circle
ctx.beginPath();
ctx.arc(300, 150, 50, 0, Math.PI * 2);
ctx.fillStyle = "red";
ctx.fill();

// Line
ctx.beginPath();
ctx.moveTo(50, 200);
ctx.lineTo(450, 350);
ctx.stroke();
