import random
import time


def display_welcome():
    print("\n" + "=" * 55)
    print("✨ WELCOME TO THE ULTIMAZE QUIZ CHALLENGE! ✨".center(50))
    print("=" * 55)
    print("\n")

    print("Instructions:")
    print("- Choose a quiz category")
    print("- Answer multiple-choice questions")
    print("- Each correct answer is worth 10 points")
    print("- See your final score at the end")
    print("- Have fun and learn something new!\n")


def display_categories():
    print("Quiz Categories:")
    print("1. General Knowledge")
    print("2. Movies and TV Shows")
    print("3. Science and Nature")
    print("4. Video Games")
    print("5. Random Mix (questions from all categories)")
    print("6. Exit")


def get_user_choice():
    while True:
        try:
            choice = int(input("\nSelect a category (1/6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Please enter between 1 and 6")
        except ValueError:
            print("Please enter number only ❌")


def load_questions():
    general_knowledge = [
        {
            "question": "Drinking a morning coffee/tea is good for health?",
            "options": ["A. Excellent", "B. No", "C. Good", "D. Natural"],
            "answer": "B"
        },
        {
            "question": "What is the capital of Australia?",
            "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"],
            "answer": "C"
        },
        {
            "question": "Which language is the most widely spoken in the world?",
            "options": ["A. English", "B. Spanish", "C. Hindi", "D. Mandarin"],
            "answer": "D"
        },
        {
            "question": "How many continents are there?",
            "options": ["A. Five", "B. Six", "C. Seven", "D. Eight"],
            "answer": "C"
        },
        {
            "question": "What color are zebra crossings?",
            "options": ["A. Black and Yellow", "B. Red and White", "C. White and Black", "D. Blue and White"],
            "answer": "C"
        }
    ]

    movies_and_tv_shows = [
        {
            "question": "Who played Iron Man in the Marvel Cinematic Universe?",
            "options": ["A. Chris Evans", "B. Robert Downey Jr.", "C. Chris Hemsworth", "D. Mark Ruffalo"],
            "answer": "B"
        },
        {
            "question": "Which TV show features a coffee shop called Central Perk?",
            "options": ["A. Seinfeld", "B. Friends", "C. How I Met Your Mother", "D. The Big Bang Theory"],
            "answer": "B"
        },
        {
            "question": "In what year was the first Harry Potter movie released?",
            "options": ["A. 2000", "B. 2001", "C. 2002", "D. 2003"],
            "answer": "B"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": ["A. James Cameron", "B. Quentin Tarantino", "C. Christopher Nolan", "D. Steven Spielberg"],
            "answer": "C"
        },
        {
            "question": "Which movie won the Best Picture Oscar in 2020?",
            "options": ["A. Joker", "B. 1917", "C. Parasite", "D. Ford v Ferrari"],
            "answer": "C"
        }
    ]

    science_and_nature = [
        {
            "question": "What planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "options": ["A. Oxygen", "B. Hydrogen", "C. Carbon Dioxide", "D. Nitrogen"],
            "answer": "C"
        },
        {
            "question": "How many bones are in the human body?",
            "options": ["A. 206", "B. 201", "C. 210", "D. 208"],
            "answer": "A"
        },
        {
            "question": "What is the boiling point of water in Celsius?",
            "options": ["A. 90°C", "B. 95°C", "C. 100°C", "D. 105°C"],
            "answer": "C"
        },
        {
            "question": "Which organ pumps blood throughout the body?",
            "options": ["A. Brain", "B. Liver", "C. Heart", "D. Kidney"],
            "answer": "C"
        }
    ]

    video_games = [
        {
            "question": "Which video game franchise features a character named Link?",
            "options": ["A. Final Fantasy", "B. The Legend of Zelda", "C. God of War", "D. Assassin’s Creed"],
            "answer": "B"
        },
        {
            "question": "What is the name of the virtual world in 'Minecraft'?",
            "options": ["A. The Grid", "B. The Realm", "C. The Nether", "D. The Block"],
            "answer": "C"
        },
        {
            "question": "Which company developed the game Fortnite?",
            "options": ["A. EA", "B. Epic Games", "C. Ubisoft", "D. Rockstar"],
            "answer": "B"
        },
        {
            "question": "Which game popularized the battle royale genre?",
            "options": ["A. PUBG", "B. Fortnite", "C. Call of Duty", "D. Apex Legends"],
            "answer": "A"
        },
        {
            "question": "In what year was the first PlayStation released?",
            "options": ["A. 1992", "B. 1994", "C. 1996", "D. 1998"],
            "answer": "B"
        }
    ]

    return {
        1: {"name": "General Knowledge", "questions": general_knowledge},
        2: {"name": "Movies and TV Shows", "questions": movies_and_tv_shows},
        3: {"name": "Science and Nature", "questions": science_and_nature},
        4: {"name": "Video Games", "questions": video_games},
        5: {"name": "Random Mix", "questions": random.sample(general_knowledge + movies_and_tv_shows + science_and_nature + video_games, 10)},
    }


def run_quiz(category_data):

    category_name = category_data["name"]
    questions = category_data["questions"]
    random.shuffle(questions)

    print(f"\nStarting the {category_name} Quiz")
    print("Answer each question by typing the letter of your choice (A, B, C or D).")

    score = 0
    correct_score = 0

    for i, que in enumerate(questions):
        print(f"\n\n---------- Questions {i+1}/{len(questions)} ----------")
        print(f" {que["question"]}")

        for op in que["options"]:
            print(f"{op}")

        while True:
            answer = input("Your answer (A/B/C/D): ").upper()
            if answer not in ["A", "B", "C", "D"]:
                print("❌ Please enter A,B,C or D")
            else:
                break

        correct_answer = answer == que["answer"]

        if correct_answer:
            score += 10
            correct_score += 1
            print("\n✅ Correct +10 points")
        else:
            print(f"\n❌ Wrong! The correct answer is {que["answer"]}")

        if i < len(questions) - 1:
            print("\n🔁 Next question coming up", end="")
            for _ in range(4):
                print(".", flush=True, end="")
                time.sleep(1.5)

    print("\n" + "=" * 50)
    print("QUIZ RESULT".center(50))
    print("=" * 50)
    print(f"Category: {category_name}")
    print(f"Correct Answers: {correct_score}")
    print(f"Total Score: {score}")

    percentage = (score / len(questions) * 10) * 100

    if percentage == 100:
        print("\n🏆 PERFECT SCORE! You're a quiz master! 🏆")
    elif percentage >= 80:
        print("\n✨EXCELLENT! You really knowyour stuff!")
    elif percentage >= 60:
        print("\n😊 GOOD JOB! You've got decent knowledge!")
    elif percentage >= 40:
        print("\n🤔 NOT BAD! There's room for improvement!")
    else:
        print("\n📚 KEEP LEARNING! Practice makes perfect!")

    return score


def main():
    display_welcome()

    total_score = 0
    play_game = True

    while play_game:
        display_categories()

        user_choice = get_user_choice()
        if user_choice == 6:
            print("GoodBye")
            break

        all_category_questions = load_questions()

        score = run_quiz(all_category_questions[user_choice])

        total_score += score

        if not input("Play another round?: ").lower().startswith("y"):
            print("\nThanks for playing!...")
            break


main()
