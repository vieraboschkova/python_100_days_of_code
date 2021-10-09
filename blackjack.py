############### Blackjack Project #####################

#Difficulty Normal : Use all Hints below to complete the project.
#Difficulty Hard : Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard : Only use Hints 1 & 2 to complete the project.
#Difficulty Expert : Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
from random import randint, choice

print(logo)

# Initial setup
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
number_of_cards = len(cards)

# Game start
def start_game():
    computers_cards = []
    users_cards = []
    computers_score = 0
    users_score = 0
    computer_won = False
    user_won = False

    def append_random_card(array):
        # new_card = cards[randint(0, number_of_cards-1)]
        new_card = choice(array)
        array.append(new_card)

    def get_score(playerCards):
        result = sum(playerCards)
        if result > 21 and 11 in playerCards:
            result -= 10
        return result

    def end_game():
        play_again = input("Do you want to play again? Answer Y or N: ")
        if play_again.lower() == "n":
            print("Good game!")
            return
        elif play_again.lower() == "y":
            start_game()
        else: 
            print("Not sure :) exiting!")
            return
    
    def win():
        print("You won!")
        end_game()
        return

    def loose():
        print("You Lost!")
        end_game()
        return

    def tie():
        print("It was a tie!")
        end_game()
        return

    def check_if_won(computer_score, users_score):
        if computer_score > 21 and users_score < 21:
            print(f"You have: {users_score} and computer has: {computers_score}")
            win()
            return True
        elif computer_score < 21 and users_score > 21:
            print(f"You have: {users_score} and computer has: {computers_score}")
            loose()
            return True
        elif computer_score == 21 and users_score < 21:
            print(f"You have: {users_score} and computer has: {computers_score}")
            loose()
            return True
        elif computer_score < 21 and users_score == 21:
            print(f"You have: {users_score} and computer has: {computers_score}")
            win()
            return True
        else:
            # print("Noone won!")
            return False

    def next_round(users_score, computers_score, rounds_passed_without_action = 0):
        if rounds_passed_without_action == 3: 
            tie()
            return
        # print(f"In the beginning of the round you have: {users_score} and computer has: {computers_score}")
        print(f"Your cards are: {users_cards}")
        new_card = input("QUESTION: Would you like to take a new card? Y or N: ")
        game_ended = False
        if (new_card.lower()=="y"):
            append_random_card(users_cards)
            users_score = get_score(users_cards)
            print(users_cards)
            print(f"You have after taking: {users_score}")
            game_ended = check_if_won(computers_score, users_score)
            if not (game_ended): 
                if (computers_score < 17):
                    append_random_card(computers_cards)
                    computers_score =get_score(computers_cards)
                    # print(f"Computer has after taking: {computers_score}")
                    # print(computers_cards)
                    game_ended = check_if_won(computers_score, users_score)
                    if not game_ended:
                        # print(f"You now have: {users_score} and computer has: {computers_score}")    
                        next_round(users_score, computers_score)
                else:
                    # print(f"You now have: {users_score} and computer has: {computers_score}")    
                    next_round(users_score, computers_score)

        else:
            if (computers_score < 17):
                append_random_card(computers_cards)
                computers_score =get_score(computers_cards)
                # print(f"Computer has after taking: {computers_score}")
                # print(computers_cards)
                game_ended = check_if_won(computers_score, users_score)
                if not game_ended:
                    # print(f"You now have: {users_score} and computer has: {computers_score}")    
                    next_round(users_score, computers_score)
            else:
                rounds_passed_without_action += 1
                # print(f"You now have: {users_score} and computer has: {computers_score}")
                print("""
                Next round...
                """)
                next_round(users_score, computers_score, rounds_passed_without_action)
    
    print("""
    !!!!!!NEW GAME!!!!!!
    """)

    # Deal 2 initial cards
    for position in range(2):
        append_random_card(computers_cards)
        append_random_card(users_cards)

    print(f"Your cards are: {users_cards}")
    # print(computers_cards)
    users_score = get_score(users_cards)
    computers_score = get_score(computers_cards)
    won = check_if_won(computers_score, users_score)
    if not won:
        print(f"One of the computers cards is: {computers_cards[1]}. ")
        next_round(users_score, computers_score)
    if user_won:
        print("You won!")
        end_game()
    elif computer_won:
        print("You Lost!")
        end_game()

# Init game
start_game()

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.