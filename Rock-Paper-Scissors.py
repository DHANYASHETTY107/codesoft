import random

user_choice = int(input("Enter your Choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = random.randint(0, 2)
print("Computer choice:", computer_choice)

if computer_choice == user_choice:
    print("It's a draw")
elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
    print("You lose")
else:
    print("You win")
