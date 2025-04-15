import random
print("🔤 WORD SCRAMBLER")

while True:
    word = input("Enter a word to scramble (or 'quit'): ").lower()
    if word == 'quit':
        print("👋🏻 Goodbye!")
        break

    latter = list(word)
    random.shuffle(latter)
    print(f"Scrambled: {"".join(latter)}")
