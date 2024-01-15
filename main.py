# import random module
import random

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

#Write your code below this line 👇


# make a list of 3 variables (rock, paper, scissors)
game_images = [rock, paper, scissors]

# input
print("Welcome to the Rock, Paper and Scissors game, What do you choose?")
user_choice = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors: "))

# if statements
if (user_choice >=3 or user_choice < 0):
  print("You entered an invalid value, try again!")
else:
  computer_choice = random.randint(0, 2)
  print("You chose:")
  print(game_images[user_choice])
  print("The computer chose:")
  print(game_images[computer_choice])
  if (user_choice == 0 and computer_choice == 2):
    print("You win!")
  elif (user_choice == 2 and computer_choice == 0):
    print("You lose!")
  elif (user_choice > computer_choice):
    print("You win!")
  elif (user_choice < computer_choice):
    print("You lose!")
  elif (user_choice == computer_choice):
    print("It's a draw!")