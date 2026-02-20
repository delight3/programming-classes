#Control Flow Statement
# 1. Decision making statement(if, elif, else)
age = 20
if age >= 20:
    print("You aare eligible to vote")
else:
    print("You are not eligible to vote")

# Examle:    
is_raining = False
if is_raining:
    print("Take an umbrella.")
else:
    print("Wear your sunglasses.")

#Multiple condition
temperature = 30
if temperature > 35:
    print("It's extremely hot")
elif temperature > 25:
    print("It's warm")
else:
    print("It's cool")

# Examle:
score = int(input("enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Examle: 
pet = input("What's your favorite pet? ")
if pet.lower() == "dog":
    print("Woof! Dogs are awesome.")
elif pet.lower() == "cat":
    print("Meow! Cats are cool.")
else:
    print("Nice! I like", pet, "too")



#Boolean Logic in condition
score = int(input("Enter your score: "))
attendance = int(input("enter attendance: "))
if score >= 80 and attendance >=75:
    print("You passed with distinction.")
else:
    print("You didn't meet the criteria.")



# 2. Looping statements(for, while)
#for loop
for num in range(10):
    print(num)

print("Start, Stop and Step")
for x in range(2, 15, 2):
    print(x)


# Loop Control Statements
# break
for z in range(1, 15):
    if z == 12:
        break
    print(z)

# continue
for c in range(1, 7):
    if c == 5:
        continue
    print(c)


#Iterating over a sequence
text = "greetings"
for l in text:
    print(l)
    


#While Loop
count = 2
while count <= 10:
    print(count)
    count += 2
    
#Iterating over a sequence
word = "Python"
i = 0
while i < len(word):
    print(word[i])
    i += 1              


# Example:
#Times Table Generator
num = int(input("enter a number: "))
print("Times Table of", num)
for t in range(1, 21):
    print(f"{num} x {t} = {num * t}")         