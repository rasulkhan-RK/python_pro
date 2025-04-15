import random

random_num = random.randint(1, 100)
while True:
  try:
    user_input = int(input("Guess number between 1 and 100: "))

    if user_input > random_num:
          print("Too High")
          
    elif user_input < random_num:
          print("Too Low")

    else:
          print("Congratulations! You guessed the number.")
          break
    
  except ValueError:
        print("Please enter valid number")
