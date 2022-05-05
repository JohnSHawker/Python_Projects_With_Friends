"""A program that allows a single player to play a game of Rock Paper Scissors against a computer opponent.
written by John """

import random
import os

# Added a main() so that if a wrong answer was input then the main menu automatically reboots instead of
# asking players if they want to play again.
def main():
    print("\nPlay Rock, Paper, Scissors against the computer.")
    print("\nCaPiTaLiZatiOn doesn't matter for your input.")
    print("\nInput Rock, Paper, or Scissors for your choice.")
    possible_actions = ["rock", "paper", "scissors"]
    while True:
        player1 = input("\nWhat do you choose? ")
        computer= random.choice(possible_actions)
        if player1.lower() == computer:
            # I added this to every if/elif statement because I couldn't find a better way to have it run.
            # If you are copy/pasting code there is probably a better solution, but this was my quick fix
            print(f"\nYou chose {player1}, computer chose {computer}.\n")
            print(f"Both players selected {player1}. It's a tie!")
        elif player1.lower() == "rock":
            print(f"\nYou chose {player1}, computer chose {computer}.\n")
            if computer == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif player1.lower() == "paper":
            print(f"\nYou chose {player1}, computer chose {computer}.\n")
            if computer == "rock":
                print("Paper covers rock! You Win!")
            else:
                print("Scissors cut paper! You lose.")
        elif player1.lower() == "scissors":
            print(f"\nYou chose {player1}, computer chose {computer}.\n")
            if computer == "paper":
                print("Scissors cut paper! You Win!")
            else:
                print("Rock smashes scissors! You lose.")
        elif player1.lower() != "rock" or player1.lower() != "paper" or player1 != "scissors":
            print("\nI did not understand your answer. Try again.")
            return main()
        play_again = input("\nPlay again? (y/n): ")
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        if play_again.lower() != "y":
            print ("Thanks for playing!")
            quit()
# need the main() to run the program. The if statement is there for troubleshooting and is
# the typical way you will see programs written in python.
if __name__ == "__main__":
    main()