import random
import time


def welcome_message():
    print("=== ROCK PAPER SCISSOR GAME ===")
    print("🪨 📃 ✂️ ")
    print("\nRules:")
    print("_ Rock crushes Scissors")
    print("_ Scissor cuts Paper")
    print("_ Paper cover Rock")
    print("_ First to win 3 rounds is the champion")
    print("\n-------------------------------------")


def get_user_choice():
    while True:
        print("\nMake your choice:")
        print("1. Rock 🪨")
        print("2. Paper 📃")
        print("3. Scissor ✂️")

        try:
            choice = int(input("Enter you choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter number only")
        except ValueError:
            print("❌  Please enter a valid number")


def get_computer_choice():
    return random.randint(1, 3)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif ((user_choice == 1 and computer_choice == 3) or
            (user_choice == 2 and computer_choice == 1) or
          (user_choice == 3 and computer_choice == 2)):
        return 'user'
    else:
        return 'computer'


def convert_text(choice):
    options = {1: "Rock 🪨", 2: "Paper 📃", 3: "Scissor ✂️"}
    return options[choice]


def display_winner(user_choice, computer_choice, result):
    user_text = convert_text(user_choice)
    computer_text = convert_text(computer_choice)

    print(f"\nYou'r choice {user_text}")
    print(f"Computer is chosing", end='')
    for _ in range(3):
        print(".", end='', flush=True)
        time.sleep(0.5)

    print(f"Computer choice {computer_text}")

    if result == 'tie':
        print("\nIt's a tie 🤝")
    elif result == 'user':
        print("\nYou won this round 🎉")
    else:
        print("\nComputer won this round 💻")


def play_game():
    welcome_message()

    user_score = 0
    computer_score = 0
    target = 3
    curr_round = 1

    while user_score < target and computer_score < target:
        print(f"\n===Round {curr_round}")
        print(f"Score: You {user_score} - {computer_score} Computer")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)
        display_winner(user_choice, computer_choice, result)

        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1

        curr_round += 1

    print("\n=== Game Over ===")
    print(f"Final score you {user_score} - {computer_score} Computer")

    if user_score > computer_score:
        print("🎉  Congrats! You are the winner")
    else:
        print("😢 Better luck next time! Computer win the game")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again.startswith('y'):
        play_game()
    else:
        print("Thanks for playing")


play_game()
