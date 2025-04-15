print("🔀 REVERSE NAME")

while True:
    name = input("\nEnter a name: ")
    if not name:
        break

    reversed_name = name[::-1]
    print(f"Your reverse name is {reversed_name}")
    print(f"The parellal universe, they call you {reversed_name.title()}")

    answer = input("\nDo you want try another? (y/n): ").lower()
    if answer != "y":
        print("Good bye")
        break
