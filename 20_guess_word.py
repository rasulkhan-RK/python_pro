import random

print("GUESS THE WORD 🤔")

words = ["python", "game", "learn",
         "fun", "enjoy", "coding", "computer", "live"]

while True:
    original_word = random.choice(words)
    latters = list(original_word)
    random.shuffle(latters)
    scrambled = "".join(latters)
    print(f"Scrambled word: {scrambled}")

    guess = input("Guess the scrambled word? ").lower()

    if guess == original_word:
        print("Congrats You Win! 🏆")
    else:
        print(f"🥲  Sorry the scrambled word is {original_word}")

    again = input("Guess again scrambled word (y/n): ").lower()
    if not again.startswith("y"):
        print("Thank you for playing 🙏🏻")
        break
