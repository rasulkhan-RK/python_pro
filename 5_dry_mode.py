import random

ROCK = 'r'
SCISSOR = 's'
PAPER = 'p'

emojis = {ROCK: '🪨', PAPER: '📃', SCISSOR: '✂️'}
choices = tuple(emojis.keys())

def get_user_choice():
  while True:
    user_choice = input("Rock, paper, or scissor? (r/p/s): ").lower()
    if user_choice in choices:
      return user_choice
    else:
      print("Invalid Entered...!")

def get_choices(user_choice, computer_choice):
  print(f"Your Choice {emojis[user_choice]}")
  print(f"Computer Choice {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    print("Tie...!")
  elif(
      (user_choice == ROCK and computer_choice == SCISSOR) or
      (user_choice == SCISSOR and computer_choice == PAPER) or
      (user_choice == PAPER and computer_choice == ROCK )
  ):
    print("You win...!")
  else:
    print("Computer Wins...!")
  

def play_game():
  while True:
    user_choice = get_user_choice()
    computer_choice = random.choice(choices)

    get_choices(user_choice, computer_choice)
    determine_winner(user_choice, computer_choice)

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == 'n':
      print("Thank you for playing")
      break


play_game()