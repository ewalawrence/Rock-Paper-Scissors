# Rock Paper Scissors

import random

options = ("rock", "paper", "scissors")
running = True

while running: 
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter an choice (rock, paper, scissors): ")

    print(f"player's choice: {player}")
    print(f"computer's choice: {computer}")

    if player == computer:
        print("It's a tie!🧛‍♂️")
    elif player == "rock" and computer == "scissors":
        print("You win!🍷")
    elif player == "paper" and computer == "rock":
        print("You win!🥇")
    elif player == "scissors" and computer == "paper":
        print("You win!🏆")
    else:
        print("You lose!😆")

    playAgain = input("Play again? (y/n): ").lower()
    if not playAgain == "y":
        running = False
print("Thanks for playing!🙏")