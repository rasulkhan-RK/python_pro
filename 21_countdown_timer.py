import time
print("COUNT DOWN ⌚")
print("Count down from your choosen seconds")

while True:
    try:
        seconds = int(input("\nEnter seconds to countdown from? "))

        if seconds <= 0:
            print("❌ Please enter a positive number")
            continue

        print(f"Count down starts from {seconds} seconds")

        for i in range(seconds, 0, -1):
            print(f"{i} seconds remaining...")
            time.sleep(1)

        print("COUNTDOWN COMPLETE ⌛")

        again = input("Start another countdown? (y/n): ").lower()

        if not again.startswith("y"):
            print("Goodbye! 👋🏻")
            break

    except ValueError:
        print("❌ Please enter a number")
