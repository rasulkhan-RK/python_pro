#Modularizing Rock, Paper, or Scissor Game
import random
choice = ('r', 'p', 's')
emojis = {'r': '🪨', 'p':'📃', 's': '✂️'}


def get_user_choice():
  while True:
    user_choice = input("Rock, paper, or scissor? (r/p/s): ").lower()
    if user_choice in choice:
      return user_choice
    else:
      print("Invalid Input try again.!")

def dispaly_choices(user_choice, computer_choice):
  print(f"Your Choice {emojis[user_choice]}")
  print(f"Computer Choice {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    print("Tie..!")
  elif(
    (user_choice == 's' and computer_choice == 'p') or
    (user_choice == 'r' and computer_choice == 's') or
    (user_choice == 'p' and computer_choice == 'r')):
    print("You Win...!")

def play_game():
  while True:
    user_choice = get_user_choice()
    computer_choice = random.choice(choice)

    dispaly_choices(user_choice, computer_choice)
    determine_winner(user_choice, computer_choice)

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == 'n':
      print('Thank you for playing...!')
      break

play_game()





