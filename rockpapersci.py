
import random

def rockpapersc(user_choice, computer_choice):
    if user_choice == 1 and computer_choice == "rock":
        print("it's a tie!")
    elif user_choice == 1 and computer_choice == "paper":
        print("you lose!")
    elif user_choice == 1 and computer_choice == "scissors": 
        print("you win!")
    elif user_choice == 2 and computer_choice == "rock":
        print("you win!")
    elif user_choice == 2 and computer_choice == "paper":
        print("it's a tie!")
    elif user_choice == 2 and computer_choice == "scissors":
        print("you lose!")
    elif user_choice == 3 and computer_choice == "rock":
        print("you lose!")
    elif user_choice == 3 and computer_choice == "paper":
        print("you win!")
    elif user_choice == 3 and computer_choice == "scissors":
        print("it's a tie!")

 

options = ["rock", "paper", "scissors"]

user_choice = int(input("Enter your choice (1-rock, 2-paper, 3-scissors, 0-exit): "))

while user_choice != 0:
    computer_choice = random.choice(options)
    if user_choice == 1:
        print("you chose rock")
    elif user_choice == 2:
        print("you chose paper")
    elif user_choice == 3:
        print("you chose scissors")

        
    print(f"Computer chose: {computer_choice}")
    rockpapersc(user_choice, computer_choice)
    user_choice = int(input("Enter your choice (1-rock, 2-paper, 3-scissors, 0-exit): "))

print("thanks for playing!")