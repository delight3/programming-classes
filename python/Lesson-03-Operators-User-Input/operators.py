# Types of Operators in Python
# 1. Arithmetic Operators
# Addition
a1 = 2
a2 = 5
print(a1 + a2)
# Subtraction
b1 = 10
b2 = 5
print(b1 - b2)
# Multiplication
c1 = 5
c2 = 2
print(c1 * c2)
# Division
d1 = 5
d2 = 2
print(d1 / d2)
# Floor Division
e1 = 7
e2 = 2
print(e1 // e2)
# Modulus (Remainder)
f1 = 5
f2 = 3
print(f1 % f2)
# Power
g1 = 5
g2 = 3
print(g1 ** g2)

# 2. Comparison Operators(check things--yes/no answers)
# Equal to
h1 = 10
h2 = 10
print(h1 == h2)

# Not equal to
i1 = 20
i2 = 15
print(i1 != i2)

# Greater than
j1 = 6
j2 = 4
print(j1 > j2)

# Less than
k1 = 7
k2 = 5
print(k1 < k2)

# Greater or equal
l1 = 9
l2 = 9
print(l1 >= l2)

# Less or equa;
m1 = 3
m2 = 6
print(m1 <= m2)

# 3. Logical Operators (Think "AND", "OR", "NOT")
# and -- BOTH must be true
is_sunny = True
finished_homework = True
can_play_outside = is_sunny and finished_homework
print("Can i play outside?", can_play_outside)

# or -- ONE must be true
have_cake = False
have_ice_cream = True
can_eat_dessert = have_cake or have_ice_cream
print("Can I eat dessert?", can_eat_dessert)

# not --Opposite
is_raining = False
can_go_to_park = not is_raining
print("Can I go to the park?", can_go_to_park)


# User Input in Python
name = input("Enter your name: ")
print(name)


# To perform calculations, user input must be converted.

# Converting to Integer:
age = int(input("Enter your age: "))
print(age)

# Converting to Float:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)