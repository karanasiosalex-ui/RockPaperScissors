rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choice_player = input("Player 1 choose rock, paper or scissors:\n ").lower()
possible_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_choices)
game_images = {"rock": rock, "paper": paper, "scissors": scissors}
print(game_images[choice_player])
print(game_images[computer_choice])


print(f"Computer's choice: {computer_choice}")
if choice_player == computer_choice:
    print("It's a tie!")
elif choice_player == "rock" and computer_choice == "paper":
    print("Computer wins!")
elif choice_player == "paper" and computer_choice == "scissors":
    print("Computer wins!")
elif choice_player == "scissors" and computer_choice == "rock":
    print("Computer wins!")
elif choice_player == "scissors" and computer_choice == "paper":
    print("You win!")
elif choice_player == "paper" and computer_choice == "rock":
    print("You win!")
elif choice_player == "rock" and computer_choice == "scissors":
    print("You win!")
else:
    print("It's invalid!")