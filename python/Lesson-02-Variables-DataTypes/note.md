Lesson 02 Notes: Variables & Data Types

What is a Variable?
A variable is a named container used to store data in a program.  
It allows us to save information, reuse it, and change it while the program is running.

Why Variables Are Important
Variables help us to:
- Store user information
- Perform calculations
- Avoid repeating values
- Make programs flexible and dynamic

Without variables, programs would be hard-coded and not useful.


Think of a variable as a label attached to a value stored in memory.

Example:

name = "John"

Explanation:

name: variable name

=: assignment operator (used to assign a value)

"John": value stored in the variable


Variable Naming Rules

Variable names must follow these rules:

Allowed:
Must start with a letter or underscore (_)

Can contain letters, numbers, and underscores

student = "John"
student_name = "Sara"
_age = 25


case-sensitive
Name = "John"
name = "Peter"

print(Name)
print(name)


Not Allowed:

Cannot start with a number

Cannot contain spaces

Cannot use special characters like @, #, $

2name = "Peter"
student name = "Ali"
total$ = 50



A data type defines the type of value a variable holds.
Python automatically assigns a data type when a value is stored.


Integer (int)
Whole numbers without decimal points.
age = 18
score = 100


Float (float)
Numbers with decimal points.
height = 5.6
price = 19.99

String (str)
Text values written inside quotes.
name = "Sabina"
message = "Learning Python"

Boolean (bool)
Represents True or False values.
is_student = True
is_logged_in = False


Checking a Variable’s Data Type
Use the type() function to check a variable’s data type.
age = 20
print(type(age))


Dynamic Typing in Python

Python is dynamically typed, meaning:
You do not declare data types explicitly
A variable can change its data type
value = 10
value = "Ten"
print(value)


Key Notes for Students

Variable names should be meaningful
Always follow naming rules
Python assigns data types automatically
Practice writing variables daily
