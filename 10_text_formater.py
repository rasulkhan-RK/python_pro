print("💬 Text Formater")
text = input("🤷‍♂️ Please enter some text? ")
if text == "":
    text = input("🤷‍♂️ Please enter some text? ")
print("1. UPPERCASE")
print("2. lowercase")
print("3. Title case")
print("4. Sentence case")

chose = input("Please chose between 1-4: ")
if chose == "":
    chose = input("Please chose between 1-4: ")
if chose == "1":
    print(text.upper())
elif chose == "2":
    print(text.lower())
elif chose == "3":
    print(text.title())
elif chose == "4":
    print(text.capitalize())
else:
    chose = input("Please chose between 1-4: ")
