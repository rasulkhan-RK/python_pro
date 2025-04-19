import time
import random

word_pairs = {
    "sky": ["blue", "sun", "cloud", "bird", "fly"],
    "water": ["drink", "ocean", "swim", "fish", "boat"],
    "food": ["eat", "cook", "tasty", "meal", "restaurant"],
    "music": ["song", "dance", "listen", "band", "rhythm"],
    "book": ["read", "stort", "page", "author", "library"],
    "tree": ["leaf", "green", "forest", "wood", "shade"],
    "car": ["drive", "ride", "wheel", "travel", "speed"],
    "dog": ["pet", "bark", "walk", "loyal", "puppy"]
}

print("WORD ASSOCIATION GAME 💪🏻")
print("Quickly, guess the prompt!")

# variables
score = 0
round = 0

while True:
    # genarating random promt words
    prompt = random.choice(list(word_pairs.keys()))
    related_word = word_pairs[prompt]

    # responsing related random words
    print(f"\nPrompt word: {prompt.upper()}")
    print("Quick, type a word related to this prompt!")

    # response time
    start_time = time.time()
    # if the user type "  hello   " it convert like this "hello"
    response = input("> ").lower().strip()
    response_time = time.time() - start_time

    print(f"Response time: {response_time}")

    # Check if response is related
    if response in related_word:
        points = max(1, 5 - int(response_time))
        score += points
        print(
            f"🤜🏻  Good association! +{points} points (answerd in {response_time:.1f}s)")
    else:
        print(
            f"❌  Not a common association, Related words included: {''.join(related_word)} ")

        round += 1
        print(f"Score: {score}/{round * 5} possible points")

    # ask to play agin
    if input("↪️  Play again? (yes/no): ").lower().startswith("n"):
        print(f"Final score: {score}. Thanks for playing! 👋🏻")
        break
