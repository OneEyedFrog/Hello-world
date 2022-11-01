import random

options = "rock", "paper", "scissors"

user_count = 0
computer_count = 0
tie_count = 0
total_count = 0
while True:
    total_count += 1
    computer_choice = random.choice(options)
    user_choice = input("Choose rock, paper, scissors, or exit: ")
    if user_choice == "rock" and computer_choice == "scissors":
        print(f"computer_choice is : {computer_choice}")
        print("You won")
        print("Rock beat scissors\n")
        user_count += 1
        continue
    elif user_choice == "scissors" and computer_choice == "paper":
        print(f"computer_choice is : {computer_choice}")
        print("You won")
        print("Scissors beat paper\n")
        user_count += 1
        continue
    elif user_choice == "paper" and computer_choice == "rock":
        print(f"computer_choice is : {computer_choice}")
        print("You won")
        print("paper beat rock\n")
        user_count += 1
        continue
    elif user_choice == computer_choice:
        print(f"computer_choice is : {computer_choice}")
        print("It's a tie\n")
        tie_count += 1
        continue
    elif user_choice == "exit":
        break
    else:
        print("You lost")
        print(f"computer_choice is : {computer_choice}\n")
        computer_count += 1
        continue

print(f"user won {user_count} times")
print(f"computer won {computer_count} times ")
print(f"Tie at {tie_count} times")
print(f"Total count is: {total_count}")
