import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

user_input = input("Do you wanna play rock paper scissors? (Y/N): ")

if user_input.lower() == "n":
    print("Thank you for playing!")
    quit()

while True:
    hand = input("Rock, Paper, Scissors (or type quit): ").lower()

    if hand == "quit":
        break

    if hand not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_pick = random.choice(options)

    print("Computer picked", computer_pick + ".")

    if hand == computer_pick:
        print("It's a tie!")

    elif (
        (hand == "rock" and computer_pick == "scissors")
        or (hand == "paper" and computer_pick == "rock")
        or (hand == "scissors" and computer_pick == "paper")
    ):
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("\nThank you for playing!")
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
