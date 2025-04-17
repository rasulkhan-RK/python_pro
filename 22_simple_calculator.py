def add(num1, num2):
    return num1 + num2


def substraction(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0 or num1 == 0:
        print("zero is not allowed in diviosion")
    return num1 / num2


def main():
    print("1. ➕  Add")
    print("2. ➖  Substraction")
    print("3. ✖️   Multiplication")
    print("4. ➗  Division")

    while True:
        choice = input("Choose method (1-4): ")
        if not choice in ["1", "2", "3", "4"]:
            print("❌ Invalid input, please try again!")
        else:
            break
    try:
        num1 = float(input("\nEnter first number? "))
        num2 = float(input("Enter second number? "))

        if choice == "1":
            print(f"\n{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"\n{num1} - {num2} = {substraction(num1, num2)}")
        elif choice == "3":
            print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"\n{num1} / {num2} = {division(num1, num2)}")

        again = input(
            "\nDo you want perform another calculation? (yes/no)? ").lower()

        if not again.startswith("y"):
            print("Goodbye 👋🏻")
            return
        else:
            main()

    except ValueError:
        print("❌ Erro! please enter valid number!")


main()
