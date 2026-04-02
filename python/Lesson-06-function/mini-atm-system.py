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