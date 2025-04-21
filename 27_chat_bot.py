import random
import time


def chatbot():
    greetings = ["Hello there! 👋🏻", "Hi, friends! 😊",
                 "Hey, Nice to meet you! 🎉", "Howdy! 😊"]

    farewells = ["Goodbye! 👋🏻", "See you latter! 🤘🏻",
                 "Bye bye! 👋🏻", "Untill next time! ✨"]

    jokes = ["I asked my dog what’s two minus two.He said nothing. 🐶",
             " accidentally rubbed ketchup in my eyes… Now I have Heinzsight. 🍅",
             "I told my computer I needed a break… It gave me a 404. 💻",
             "My phone battery lasts longer than most relationships these days. 🔋💔",
             "Why don’t oysters donate to charity?Because they’re shellfish. 🦪",
             "I bought a ceiling fan the other day.Complete waste of money — he just stood there and clapped.",
             "If life gives you melons, you might be dyslexic. 😅"
             ]

    facts = ["Bananas are berries, but strawberries aren't. 🍌🍓 Yeah, science is just   messing with us now.",
             "A day on Venus is longer than a year on Venus. 🌍⌛ It spins so slowly that it rotates once every 243 Earth days, but orbits the sun every 225.",
             "Octopuses have three hearts. ❤️❤️❤️ Two pump blood to the gills, one to the rest of the body. Also, they taste with their arms!", "There’s a species of jellyfish that can technically live forever. 🧬 Turritopsis dohrnii can revert its cells back to an earlier stage when it's hurt or aging.",
             "The shortest war in history lasted 38–45 minutes. ⚔️ Between Britain and Zanzibar in 1896. (Spoiler: Zanzibar lost.)", "Humans glow in the dark — very faintly. ✨ It’s called bioluminescence, but it's 1,000 times weaker than our eyes can detect."]

    bot_name = "Chatbot"
    print(f"{bot_name} is starting...")
    time.sleep(1)

    print(f"""
          💬 Welcome to {bot_name}! 💬

          I can chat about:
          🃏  'joke' - Here a funny joke
          🫠   'facts' - Learn something new
          ©️   'color' - My favorite color
        👋🏻  'bye' - End our chat
         \n""")

    chating = True
    user_name = input(
        f"Hello my name is {bot_name}! What's your name: ").lower().strip()
    print(
        f"\n{bot_name} nice to meet you {user_name.title()} how can i help you today?")

    while chating:
        user_input = input("You: ").strip()

        if user_input in ["hi", "hello", "hey", "howdy"]:
            print(f"💬 {bot_name}: {random.choice(greetings)}")
        elif "joke" in user_input:
            print(f"💬 {bot_name}: {random.choice(jokes)}")
        elif "facts" in user_input:
            print(f"💬 {bot_name}: {random.choice(facts)}")
        elif "color" in user_input:
            print(
                f"💬 {bot_name}: My favaorite color is blue 🔵! What's your favarite color?")
            color = input("You'r color: ").strip().title()
            print(f"💬 {bot_name}: {color} is a great color")

        elif user_input in ["bye", "exit", "quit", "goodbye"]:
            print(f"💬 {bot_name}: {random.choice(farewells)}")
            print(f"💬 {bot_name}: it was fun chating with you, {user_name}")
            chating = False

        else:
            responces = ["That's interasting tell me more.",
                         "I'm not sure I undestand, Can you try again",
                         "Hmm, Let's talk about something else, Try asking for a joke or fact", "Beep boop! My robot brain is processing that 😆"]
            print(f"💬 {bot_name}: {random.choice(responces)}")

    print(f"Thanks for chatting run the program again to talk me latter! 👋🏻")


chatbot()
