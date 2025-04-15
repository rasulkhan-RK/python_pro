print("🔡 VOWEL COUNTER")

# Simple syntax
while True:
    text = input("Enter a some text or ('quit'): ").lower()
    if text == 'quit':
        print("👋🏻 Good bye")
        break

    vowel_count = 0
    for latters in text:
        if latters in ["a", "e", "i", "o", "u"]:
            vowel_count += 1

    print(f"That text has {vowel_count} vowels!")
