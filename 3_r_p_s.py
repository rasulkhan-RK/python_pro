import random

choise = ('r', 'p', 's')
emojis = {'r': '🪨', 'p':'📃', 's': '✂️'}

while True:
  user_choise = input("Rock, paper, or scissor? (r/p/s): ")
  if user_choise not in choise:
    print("Invalid Entered")
    continue

  comuter_choise = random.choice(choise)
  print(f"You Chose {emojis[user_choise]}")
  print(f"Computer Chose {emojis[comuter_choise]}")

#Determine the winner
  if user_choise == comuter_choise:
    print("Tie...!")
  elif(
    (user_choise == 's' and comuter_choise == 'p') or 
    (user_choise == 'p' and comuter_choise == 'r') or
    (user_choise == 'r' and comuter_choise == 's')):
    print("You Win...!")
  else:
    print("You Lose...!")

#Should continue game
  should_continue = input("Continue? (y/n): ")
  if should_continue == 'n':
    print("Thank you for playing!!!")
    break
