print("CHECK CHARACTER TYPE")
char = input("Please enter character and check: ")

if char == "":
    char = input("Please enter character and check: ")

if char.isalpha():
    print("This is a character")
elif char.isdigit():
    print("This is a digit")
else:
    print("This is special symbol")
