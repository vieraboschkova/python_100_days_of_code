from art import logo
from random import randint
# Print logo

print(logo)

# Welcome screen
print("Welcome to the guessing game!")
game_on = True

while game_on:
    # Choose a random number between 1 - 100
    number_to_guess = randint(1,100)
    was_number_guessed = False
    print(number_to_guess)

    # Choose difficulty level
    # assign number of tries
    difficulty_level = input("Want it easy or hard? Type E or H. ").lower()
    number_of_tries_left = 10
    if difficulty_level == "h":
        number_of_tries_left -= 5
        print(f"Hard chosen! Tries left: {number_of_tries_left}")
    elif difficulty_level == "e":
        print(f"Easy chosen! Tries left: {number_of_tries_left}")
    else:
        print(f"No correct level chosen. Starting with easy. Tries left: {number_of_tries_left}")

    # ask for a guess
    while number_of_tries_left > 0 and not was_number_guessed:
        guessed_number = int(input("What are you thinking that I'm thinking? Type a number: "))
        # check if lower/higher/exact
        # if exact - won -> end game -> ask if plays again
        if guessed_number == number_to_guess:
            was_number_guessed = True
            print(f"Yay! You won! It was: {number_to_guess}")
        elif guessed_number > number_to_guess:
            number_of_tries_left -= 1
            print(f"Too high! You have: {number_of_tries_left} chances left")
        elif guessed_number < number_to_guess:
            number_of_tries_left -= 1
            print(f"Too low! You have: {number_of_tries_left} chances left")
        # decrease number of tries
        # repeat
        # if no more number of tries - > lost -> ask if plays againa
    
    go_again = input("Would you like to go again? Type Y or N. ").lower()
    if go_again == "n":
        game_on = False
        print("Bye bye! Good game!")