import random
import os

while True:
    possible_actions = ["rock", "paper", "scissors"]
    print("\nPlay Rock, Paper, Scissors against the computer.")
    print("\nCaPiTaLiZatiOn doesn't matter for your input.")
    print("\nInput Rock, Paper, or Scissors for your choice.")
    player1 = input("\nWhat do you choose? ")
    if player1.lower() != "rock" or player1.lower() != "paper" or player1 != "scissors":
        print("\nI did not understand your answer. Try again.")
        wait = input("press Enter to continue.")
    computer= random.choice(possible_actions)
    print(f"\nYou chose {player1}, computer chose {computer}.\n")

    if player1.lower() == computer:
        print(f"Both players selected {player1}. It's a tie!")
    elif player1.lower() == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player1.lower() == "paper":
        if computer == "rock":
            print("Paper covers rock! You Win!")
        else:
            print("Scissors cut paper! You lose.")
    elif player1.lower() == "scissors":
        if computer == "paper":
            print("Scissors cut paper! You Win!")
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("\nPlay again? (y/n): ")
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()
    if play_again.lower() != "y":
        print ("Thanks for playing!")
        quit()