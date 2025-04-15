print("🧮 GRADE CALCULATOR")
scores = []

while True:
    score = input("Please enter a test score (or 'done'): ").lower()
    if score == 'done':
        print("👋🏻 Good Bye!")
        break
    scores.append(float(score))
    average = sum(scores) / len(scores)

    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    else:
        print("Grade: D or F")
