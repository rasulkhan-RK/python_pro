import os
import time
import random


def clear_screen():
    """CLEAR THE SCREEN OR TERMINAL"""
    os.system('cls' if os.name == 'nt' else 'clear')


print("🧠  MEMORY SEQUENSE GAME 🧠")
print("Remember the sequense and type it back! ✨")
print("\nRules:")
print("_ Watch as numbers appear one by one")
print("_ After the sequence is shown, type it back in order")
print("_ Each rounds adds one more number to remember")
print("_ How far can you go? 🏆")

input("Press enter to start....")

sequence = []
current_round = 1
game_over = False

while not game_over:
    sequence.append(random.randint(1, 9))

    clear_screen()
    time.sleep(0.7)

    for number in sequence:
        time.sleep(0.7)
        print(f"\n{number}")
        time.sleep(0.7)
        clear_screen()

    print(f"=== Round {current_round} ===")
    print("Remember the sequence and re-enter the number, seprated by space:")
    player_answer = input("> ")

    try:
        player_sequence = [int(num) for num in player_answer.split()]
    except ValueError:
        print("❌  Please enter number only")
        game_over = True
        continue

    if player_sequence == sequence:
        print(f"✨  Congrats! You remember all {len(sequence)} numbers")
        current_round += 1
        time.sleep(2)
    else:
        print(f"😢  Game over! You remember all {current_round - 1} numbers")
        print(
            f"The correct sequence are {" ".join(str(num) for num in sequence)}")
        game_over = True

    if game_over:
        play_again = input("Play again? (yes/no): ").lower()
        if play_again.startswith('y'):
            sequence = []
            current_round = 1
            game_over = False
        else:
            print('👋🏻  Thanks for playing')
