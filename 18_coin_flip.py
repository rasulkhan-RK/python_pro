
import random

print("🪙 COIN FLIP GAME 🪙")
print("Guess heads or tails")

while True:
    guess = input("\nEnter your guess (heads/tails): ").lower()
    if guess != 'heads' and guess != 'tails':
        print("Please enter 'heads' or 'tails' ❌")
        continue
    elif guess == "":
        print("Please enter 'heads' or 'tails' ❌")
        continue

    flip = random.choice(['heads', 'tails'])

    if flip == guess:
        print("You won, you guessed correctly 💐")
    else:
        print("Sorry, wrong guess. Try again! 🌳")

    again = input("Guess again (yes/no): ").lower()
    if not again.startswith("y"):
        print("Good bye 👋🏻")
        break
