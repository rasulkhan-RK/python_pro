print("🏃🏻‍♂️‍➡️ Step Counter 🏃🏻‍♂️")
daily_goal = int(input("🤷‍♂️ What is your daily step goal? "))
current_step = int(input("✨ How many steps do you have taken today? "))

remaining_steps = daily_goal - current_step

if remaining_steps > 0:
    print(f"💪🏻 You need {remaining_steps} more steps to reach your goal!")
else:
    print(
        f"😊 Congratulations! You've exceeded your goal {-remaining_steps} steps")
