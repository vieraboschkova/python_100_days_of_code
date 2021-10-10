from art import logo, vs
from game_data import data
from random import randint

NUMBER_OF_DATA = len(data)

# Helper function: check answer and say if it was correct
def check_is_answer_correct(followers_of_A, followers_of_B, given_answer):
    """Checks answer against given data. 
        Returns boolean that say if the answer was correct."""
    is_A_higher = followers_of_A > followers_of_B
    if (given_answer == "a" and is_A_higher) or (given_answer == "b" and not is_A_higher):
        return True
    else:
        return False

def get_second_index(a_index):
    """Assigns second random index in the range of data. 
        If it is the same as a_index, searches for a different one."""
    b_index = randint(0, NUMBER_OF_DATA - 1)
    while a_index == b_index:
        b_index = randint(0, NUMBER_OF_DATA - 1)
    return b_index

def game():
    """Compares the followers on instagram. If you guess correctly, compares a next pair.
        If not, the game ends and score is shown.
    """
    print(logo)
    # set score to 0 and set game to continue
    score = 0
    game_on = True
    search_A_index = randint(0, NUMBER_OF_DATA - 1)
    search_B_index = get_second_index(search_A_index)
    # get first two questions
    while game_on:
        print(f"A: {data[search_A_index]['name']}, {data[search_A_index]['description']}, from {data[search_A_index]['country']}")
        print(vs)
        print(f"B: {data[search_B_index]['name']}, {data[search_B_index]['description']}, from {data[search_B_index]['country']}")
        
        # get answer
        guess = input("Who do you think has more followers? Type A or B: ").lower()
        # compare answers
        is_guess_correct = check_is_answer_correct(
            data[search_A_index]['follower_count'],
            data[search_B_index]['follower_count'],
            guess,
        )
        # assign score/ loose and show score
        if not is_guess_correct:
            game_on = False
            print(f"INCORRECT! Your score was: {score}")
        # if not loose -> next question
        # repeat
        else:
            score += 1
            search_A_index = search_B_index
            search_B_index = get_second_index(search_A_index)
            print("CORRRRRECT! Starting next round!")

game()