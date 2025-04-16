import random

print("RECIPE GENERATER 😋")

protiens = ['chicken', 'fish', 'tuna', 'beef', 'eggs']
veggies = ['carrots', 'spinach', 'mashrooms', 'bell peppers', 'broccolli']
carbs = ['rice', 'pasta', 'potatoes', 'bread', 'quiona']
methods = ['baked', 'grilled', 'stir-fried', 'souteed', 'roasted']
flavors = ['garlic', 'lemon', 'spicy', 'herb', 'sweet & sour']

while True:
    protien = random.choice(protiens)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)
    method = random.choice(methods)
    flavor = random.choice(flavors)

    print(
        f"\nYour random recipe: {flavor} {method} {protien} and {veggie} with {carb}")

    if not input("Generate another one? (y/n): ").lower().startswith('y'):
        print("👋🏻 Goodbye")
        break
