import os
import time
import datetime


DATA_FILE = "data_transaction.txt"


def add_transaction():
    while True:
        print("\nAdd Transaction")
        transaction_type = input("choose ➕ income or ➖ expences (i/e): ")

        if transaction_type in ["i", "e"]:
            break
        else:
            print("Please choice i/e")

    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ").title().strip()
    description = input("Enter description: ").title().strip()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    symbol = "+" if transaction_type.startswith("i") else "-"

    with open(DATA_FILE, "a") as file:
        file.write(f"{today}|{symbol}{amount}|{category}|{description}\n")
    print("Data saving", end="")
    for _ in range(4):
        print(".", flush=True, end="")
        time.sleep(0.9)

    print("\n✅ Transaction added successfully!\n")


def view_transaction():
    if not os.path.exists(DATA_FILE):
        print("\n❌ No transaction found! ❌\n")
        return

    print("-" * 60)
    print("TRANSACTION")
    print("-" * 60)

    print("Date              Amount            Category         Description")
    with open(DATA_FILE, "r") as file:
        for line in file:
            parts = line.split("|")
            date = parts[0]
            amount = parts[1]
            category = parts[2]
            description = parts[3]
            symbol = "💵" if amount.startswith("+") else "🥀"

            print(
                f"{date}      |{symbol} {amount}        |{category}          |{description}")


def get_summary():
    if not os.path.exists(DATA_FILE):
        print("No transaction found! ❌")
        return

    total_income = 0
    total_expences = 0

    with open(DATA_FILE, "r") as file:
        for line in file:
            parts = line.split("|")
            amount = parts[1]

            if amount.startswith("+"):
                total_income += float(amount[1:])
            else:
                total_expences += float(amount[1:])

    balance = total_income - total_expences

    print("-" * 60)
    print("SUMMARY")
    print("-" * 60)
    print(f"Total Income:", total_income)
    print(f"Total Expences:", total_expences)
    print(f"Remaining Balance:", balance)
    print("\n")


def main():
    print("\n" + "=" * 30)
    print("®️  FINANCE TRACKER ®️")
    print("=" * 30)

    while True:
        print("1. ➕  Add Transaction")
        print("2. 🪟  View Transaction")
        print("3. 💁🏻‍♂️  Summary")
        print("4. 📕  Exit")

        choice = input("Choice (1-4): ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transaction()
        elif choice == "3":
            get_summary()
        elif choice == "4":
            print("\nGoodbye 👋🏻\n")
            break
        else:
            print("Invalid choice, please between 1-4")


main()
