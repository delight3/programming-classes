Lesson 04 Notes: Strings and Numeric Functions

What is a String?
A string is a sequence of characters used to represent text.
Strings are written inside single or double quotes.

Example:
python
name = "Sabina"
message = 'Welcome to Python'

Basic String Operations
String Concatenation

Joining strings together using +.
first_name = "Jane"
last_name = "Peter"
full_name = first_name + " " + last_name
print(full_name)


String Repetition

Repeating a string using *.
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)


String Length

Use len() to find the number of characters
text = "Python"
print(len(text))


String Indexing

Each character in a string has an index starting from 0
word = "Python"
print(word[0])   
print(word[3])  


String Slicing

Extracting a part of a string.
word = "Programming"
print(word[0:6])   # Progra
print(word[:4])    # Prog
print(word[4:])    # ramming


Common String Methods

Method	     Description	    Example
upper()	Converts to uppercase	text.upper()
lower()	Converts to lowercase	text.lower()
capitalize()	Capitalizes first letter	text.capitalize()
title()	Capitalizes each word	text.title()
strip()	Removes spaces	text.strip()
replace()	Replaces text	text.replace("python", "java")


Checking Text Content
text = "Python123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())

String Format
String formatting is a way to insert variables or values into strings in a clean and readable manner.  
It allows you to combine text with numbers, variables, and expressions.

Instead of writing many + operators, string formatting makes code simpler and more professional.
Example:
name = "Sabina"
age = 20

print(f"My name is {name} and I am {age} years old.")



Numeric Functions in Python

Python provides built-in functions to work with numbers.
Common Numeric Functions

Function	Description	    Example
int()	Converts to integer	int("10")
float()	Converts to float	float("3.5")
abs()	Absolute value	    abs(-10)
round()	Rounds a number	    round(3.6)
max()	Returns largest value	max(3, 7, 1)
min()	Returns smallest value	min(3, 7, 1)
sum()	Adds values	           sum([1, 2, 3])