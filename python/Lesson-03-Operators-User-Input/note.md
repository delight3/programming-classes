Lesson 03 Notes: Operators & User Input

Lesson Overview
In this lesson, students will learn how to:
- Perform operations using operators
- Understand different types of operators in Python
- Collect input from users
- Convert user input to appropriate data types

Operators allow Python to perform actions, while user input makes programs interactive.


What are Operators?
Operators are symbols used to perform operations on values and variables.


1. Arithmetic Operators

Used to perform mathematical calculations.
Operator	Name	Example
+	Addition	x + y
-	Subtraction	x - y
*	Multiplication	x * y
/	Division	x / y
%	Modulus	x % y
**	Exponent	x ** y
//	Floor Division	x // y


2. Assignment Operators

Used to assign values to variables.
Operator	Example	Meaning
=	x = 5	Assign value
+=	x += 2	x = x + 2
-=	x -= 2	x = x - 2
*=	x *= 2	x = x * 2
/=	x /= 2	x = x / 2


3. Comparison Operators

Used to compare two values.
They return True or False.
Operator	Meaning
==	Equal to
!=	Not equal
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to


4. Logical Operators

Used to combine conditional statements.
Operator	Meaning
and	 Both conditions must be True
or	 At least one condition is True
not	 Reverses the result


User Input in Python

Python uses the input() function to get data from the user.
name = input("Enter your name: ")
print(name)

Important:
input() always returns a string.

Converting User Input (Type Casting)

To perform calculations, user input must be converted.

Converting to Integer:
age = int(input("Enter your age: "))
print(age)

Converting to Float:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)

Common Errors to Avoid

- Forgetting to convert input to int or float
- Dividing by zero
- Using = instead of == in comparisons

Key Notes for Students

- Operators perform actions on values
- input() makes programs interactive
- Always convert user input when doing calculations
- Practice writing small interactive programs