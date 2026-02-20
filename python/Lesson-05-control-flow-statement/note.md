Lesson 05 Notes: Control Flow Statements

What is Control Flow?
Control flow refers to the order in which statements are executed
in a program.

By default, Python executes code line by line, but control flow
statements allow the program to:
- Make decisions
- Repeat tasks
- Skip or stop execution when needed


Types of Control Flow Statements
1. Conditional Statements
2. Looping Statements
3. Loop Control Statements


Conditional Statements
Conditional statements allow a program to make decisions based on conditions.


The if Statement
Executes a block of code if a condition is True.

age = 18

if age >= 18:
    print("You are eligible")


The if-else Statement

Executes one block if the condition is True and another if it is False.
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")


The if-elif-else Statement

Used when there are multiple conditions.
score = 75

if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")


Looping Statements

Loops allow code to run repeatedly as long as a condition is met.

The while Loop

Repeats code while a condition is True.
count = 1

while count <= 5:
    print(count)
    count += 1


The for Loop

Used to iterate over a sequence.
for i in range(1, 6):
    print(i)



Loop Control Statements

1. break
Stops the loop immediately.
for i in range(10):
    if i == 5:
        break
    print(i)



2. continue
Skips the current iteration and moves to the next.
for i in range(5):
    if i == 2:
        continue
    print(i)



Common Mistakes
- Forgetting indentation
- Infinite loops in while
- Incorrect condition logic

Key Notes for Students
- Control flow controls how a program runs
- Conditions must evaluate to True or False
- Loops should always have an exit condition
- Indentation is very important in Python