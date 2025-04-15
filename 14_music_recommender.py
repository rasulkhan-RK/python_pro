import random
print("🎶 MUSIC RECOMMENDER")

recom = {
    "rock": ["AC/DC", "Queen", "Led Zepplin"],
    "pop": ["Taylor shuf", "Ed Sheeran", "Ariana Grande"],
    "hip-hop": ["Kendrick lamar", "Drake", "J.Cole"]
}

choice = input("What music do you like? (rock/pop/hip-hop): ").lower()

if choice not in recom:
    print("🥲_ Sorry, I don't know that...")
else:
    print(f"Check out {random.choice(recom[choice])}")
