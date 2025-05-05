import random
import string
import time


def get_gen_password(
        length, use_lowercase, use_uppercase, use_numbers, use_symbols):
    char = ""

    if use_lowercase:
        char += string.ascii_lowercase
    if use_uppercase:
        char += string.ascii_uppercase
    if use_numbers:
        char += string.digits
    if use_symbols:
        char += string.punctuation

    if not char:
        print("Oops! No characters type selected. Using lowercase letters by default!")
        char = string.ascii_lowercase

    password = ""
    for _ in range(length):
        password += random.choice(char)

    return password


def get_password_strength(password):
    if len(password) >= 20:
        return "Hard"
    elif len(password) >= 15:
        return "Medium"
    elif len(password) <= 9:
        return "Lower"
    else:
        return "Normal"


def get_yes_no_input(questions):
    while True:
        response = input(questions).lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("I don't get that! Please enter 'y' or 'n'.")


def main():
    print("\n==== 🔒 PASSWORD GENERATOR 🔒 ====")
    print("✨ Create super strong and secure password with ease! ✨")

    while True:
        try:
            length = int(input("Enter password length (8-30): "))
            if 8 <= length <= 30:
                print("\n🎮Let's customize your password 🎮")
                use_lowercase = get_yes_no_input(
                    "Include lowercase letters (a-z)? (y/n): ")
                use_uppercase = get_yes_no_input(
                    "Include uppercase letters (A-Z)? (y/n): ")
                use_numbers = get_yes_no_input(
                    "Include numbers (0-9)? (y/n): ")
                use_symbols = get_yes_no_input(
                    "Include special characters (!@#$%.)? (y/n): ")

            else:
                print("⚠️ Alert length should be 8-30 ⚠️")
                continue
        except ValueError:
            print("Please enter numbers only, between 8 to 30 ❌")

        print("\n🙋🏻‍♀️ Generating your new magical password", end="")
        for _ in range(4):
            print(".", end="", flush=True)
            time.sleep(0.8)

        print("\n🎁 ==== YOUR NEW PASSWORD ==== 🎁")
        password = get_gen_password(
            length, use_lowercase, use_uppercase, use_numbers, use_symbols)
        pass_strength = get_password_strength(password)

        print(f"🔑 Password: {password}")
        print(f"Strength: {pass_strength}")

        if not input("\nGenerate again? (y/n): ").lower().startswith("y"):
            print("Thanks for using! Goodbye 👋🏻")
            break


main()
