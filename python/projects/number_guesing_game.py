import random
print(random.randint(1, 10))


def number_guessing_game():
    print('welcome to the number guesing game!')
    print("I'm thinking of a number between 1 and 100")
    
    play_game = True
    while play_game:
        number_to_guess = random.randint(1, 100)
        number_of_guesses = 0
        guessed = False
        
        while not guessed:
            guess = int(input('make a guess:')) 
            number_of_guesses += 1
            
            if guess < number_to_guess:
                print('Too low! try again')
            elif guess > number_to_guess:
                print('Too high! try again')
            else:
                print(f"Congratulations! You guessed the number in {number_of_guesses} right.")
                guessed = True
                
        play_again_input = input('Do you want to play again! (yess/no)')
        play_again = play_again_input == 'yes'
    print("Thanks for playing")                 

#Start the game
number_guessing_game()
