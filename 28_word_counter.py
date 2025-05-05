def count_words(text):
    words = len(text.split())
    return words


def count_with_space(text):
    with_space = len(text)
    return with_space


def count_without_space(text):
    without_space = len(text.replace(" ", ""))
    return without_space


def word_sentences(text):
    sentence_ending = [".", "!", "?", ","]
    count = 0

    for char in text:
        if char in sentence_ending:
            count += 1

    return count


def anlyze__text(text):
    words = count_words(text)
    with_space = count_with_space(text)
    without_space = count_without_space(text)
    sentences = word_sentences(text)

    print("\n---- Anlyze Text ----")
    print(f"Words: {words}")
    print(f"Count (with space): {with_space}")
    print(f"Count (without space): {without_space}")
    print(f"Sentences: {sentences}")


def main():
    print("📱 ==== Word Counter ==== 📱")
    print("Count words, characters and sentences to anlyze your text")

    while True:
        print("\nChoose your option")
        print("1. 📃 Enter text to anlyze")
        print("2. 🚪 Exit")

        choice = input("You'r choice (1/2): ")
        if choice == "1":
            print("Enter or paste your text to anlyze (enter twice to finish)")
            lines = []

            while True:
                line = input()
                if not line and not lines[-1]:
                    break

                lines.append(line)

            text = "\n".join(lines)
            anlyze__text(text)

        elif choice == "2":
            print("Thanks for using word counter, Goodbye 👋🏻")
            break
        else:
            print("Please choose between 1 or 2 ❌")


main()
