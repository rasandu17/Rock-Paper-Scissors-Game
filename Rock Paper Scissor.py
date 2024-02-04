import random

def print_rules():
    print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
          + "Rock vs Paper -> Paper wins \n"
          + "Rock vs Scissors -> Rock wins \n"
          + "Paper vs Scissors -> Scissor wins \n")

def get_user_choice():
    while True:
        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
        choice = int(input("Enter your choice :"))
        if 1 <= choice <= 3:
            return choice
        print('Enter a valid choice please')

def get_computer_choice():
    comp_choice = random.randint(1, 3)
    while comp_choice == get_user_choice():
        comp_choice = random.randint(1, 3)
    return comp_choice

def get_result(user_choice, comp_choice):
    if user_choice == comp_choice:
        return 'DRAW'
    elif (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1):
        return 'USER'
    else:
        return 'COMPUTER'

def print_result(result, user_choice, comp_choice):
    if result == 'DRAW':
        print("<== Its a tie ==>")
    elif result == 'USER':
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

def play_game():
    print_rules()
    while True:
        user_choice = get_user_choice()
        comp_choice = get_computer_choice()
        result = get_result(user_choice, comp_choice)
        print("User choice is \n", ['Rock', 'Paper', 'Scissors'][user_choice - 1])
        print("Computer choice is \n", ['Rock', 'Paper', 'Scissors'][comp_choice - 1])
        print_result(result, user_choice, comp_choice)
        print("Do you want to play again? (Y/N)")
        ans = input().lower()
        if ans == 'n':
            break

play_game()
