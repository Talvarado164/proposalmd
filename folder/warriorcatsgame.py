import random


def create_character():
    #Create a cat character in the warriors universe beginning with the suffix -paw to sybolize apprenticeship
    print("Welcome to a Warrior Cats text-based adventure game! Let's get our character started.")
    prefix = input("Choose a nature-based prefix! (Leaf, Snow, Fire, Ice, etc.):")
    name = prefix + "-paw"
    clan = input(f"What clan does {name} choose?")

    #Create randomized stats including strength, agility, and intelligence.
    stats = {
        "Strength": random.randint(5, 15),
        "Intelligence": random.randint(5, 15),
        "Agility": random.randint(5, 15),
    }