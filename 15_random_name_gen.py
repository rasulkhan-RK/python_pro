import random
print("✨ RANDOM NAME GENARATER")

first_part = ["John", "Mark", "Alex", "Kevin", "Admire", "Nikh", "Willson"]
second_part = ["Cena", "Dean", "Clesk", "Devine", "Zukpir", "Oiva", "Ikoma"]

count_input = input("How many name do you want? ")

if count_input.isdigit():
    count = int(count_input)
    for i in range(count):
        first_name = random.choice(first_part)
        second_name = random.choice(second_part)
        print(f"{first_name}_{second_name}")
else:
    print("Invalid count/number")
