# Creating (Defining) a Function
def greet():
    print("Hello, welcome to Python!")


greet()  # Calling (Using) a Function


# Function with Parameters
def person(name):
    print(f"Hello, {name}!")


person("Rhoda")  # Call it with an argument:


# Function with Return Value
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)
print(result)


# Return Multiple Values
def calculate(a, b):
    return a + b, a * b

sum_result, product_result = calculate(2, 3)
print(sum_result, product_result)  # Output: 5 6


# Grade calculator
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"


grade = calculate_grade(float(input("Enter your score: ")))
print('Your grade is:', grade)


# Default Parameter Value
def greet_user(name):
    print(f"Hello, {name}!")


greet_user("John")


# Arbitrary arguments (*args)
def family(*kid):
    print("The youngest child is " + kid[2])
    print(f"{kid[0]} is the first child, \n{kid[1]} is the second child, and {kid[2]} is the third child.")


family("David", "Henry", "Jane", "Elvis", "Lloyd")

# Print all the arguments passed to the function
def print_all(*args):
    for arg in args:
        print(arg)


print_all("Hello", "World", "This", "is", "a", "test")

# Keyword arguments
def person_info(name, age, state):
    print(f"Name: {name}, Age: {age}, State: {state}")


person_info(name="Alice", state="California", age=30)

# Arbitrary keyword arguments (**kwargs)
def user(**about):
    print(
        f"Name: {about['name']}, Age: {about['age']}, State: {about['state']}")


user(name="Bob", age=25, state="New York")


def show_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_info(name="Charlie", age=20, state="Texas", occupation="Student")


# Global Variables
j = "Global Variable"

def my_function():
    print(j)
    k = "Local Variable"
    print(k)


my_function()
print(j)
# print(k)  # This will raise an error because k is a local variable and cannot be accessed outside the function.

#We can create a global variable inside a function using 'global' keyword
def myfun():
    global z
    z = "greetings"
    print(z, "Henry")
myfun()
print(z + "Henry")                       


# Mini ATM System
#Function to display ATM menu option
def show_menu():
    print("Mini ATM")
    print("1. Check Balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")

#Function to display current balance
def check_balance(balance):
    print(f"Your current balance is: ${balance}")

#Function to handle deposite operation
def deposit(balance):
    amount = float(input("enter amount to desplay: $"))
    
    #Check if the amount is valid(greater than 0)
    if amount > 0:
        balance += amount #Add amount to balance
        print("Deposite successful!")
    else:
        print("Invalid amount.")
        
    return balance #Return updated balance


#Function to handle withdrawal operation
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))
    
    #Check if user is trying to withdraw more than balance
    if amount > balance:
        print("Insufficient fund!")
        
    #Check if amount is invalid (zero or negative)    
    elif amount <= 0:
        print("Invalid amount.")
    
    else:
        balance -= amount #Subtract amount from balance
        print("Withdraw successful!")
    return balance

#Main ATM function that controls the program
def atm():
    balance = 1000 #Starting balance
    
    #Infinite loop (runs until user exits)
    while True:
        show_menu() #Display menu option
        
        #Get user choice
        choice = input("Choose an option (1-4): ")
        
        #If user selects option 1
        if choice == "1":
            check_balance(balance) #show balance
            
        # If user select option 2
        elif choice == "2":
            balance = deposit(balance) #Update balance after deposite
            
        #If user select option 3
        elif choice == "3":
            balance = withdraw(balance) #Update balance after withdraw
        
        #If user select option 4
        elif choice == "4":
            print("Thanks you for using the ATM!")
            break # Exit the loop and end program
                
        else:
            print("Invalid choice. try again.")

#Run tha app(start the ATM program)            
atm()                    