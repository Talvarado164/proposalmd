import random


def create_cat():
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

    #Cats will have a unique ability that they can utilize during certain scenarios.
    print("\nChoose a unique ability:")
    print("1. Healing (Heal if points are lost after battles)")
    print("2. Extra Strength (Does more damage during a battle scenario)")
    print("3. Stealth (Ability to escape danger)")
    ability = input("What will be your unique ability? (1/2/3): ")
    abilities = {1: "Healing", 2: "Extra Strength", 3: "Stealth"}
    special_ability = abilities.get(int(ability), "Healing")

    print(f"\n{name} of {clan} has chosen {special_ability}!")
    print(f"Stats: {stats}\n")
    return name, clan, stats, special_ability


def upgrade_to_warrior(name, stats):
    #Give your character a proper warrior suffix when leveled up properly
    total_stats = sum(stats.values())
    if total_stats > 40:  
        suffixes = ["dapple", "tail", "pelt", "fur", "nose", "flight", "song", "fur"]
        new_suffix = random.choice(suffixes)
        name = name.split("-")[0] + f"-{new_suffix}"
        print(f"\nYour clan leader has decided that {name} has earned their warrior suffix!")
    else:
        print(f"\n{name} has many moons ahead to earn their warrior name.")
    return name


def hunting_scenario(name, stats):
    #Scenario 1 in this game--a simple hunting scenario that uses your stats to determine how successful the choice you make will be.
    """Scenario 1: Hunting"""
    print("Scenario 1: Hunting")
    print("You spot a bird on a branch--it looks like it is foraging for something. You think about what you should do.")
    print("1. You steathily scale up the tree and try to catch it silently (Agility needed)")
    print("2. You wait for it to leap down to continue its forage, and then you strike (Intelligence needed)")
    print("3. You leap upon the branch and catch it while it is off guard (Strength needed)")

    choice = input("Choose an option (1/2/3): ")
    if choice == "1" and stats["Agility"] > 10:
        print(f"{name} sneakily climbs up and pounces on the bird. Nice!")
        return 10
    elif choice == "2" and stats["Intelligence"] > 10:
        print(f"{name} patiently waits until the bird is on the ground and catches it. Success!")
        return 10
    elif choice == "3" and stats["Strength"] > 10:
        print(f"{name} uses great force to leap up the tree and catch the bird in their jaws. Nice job!")
        return 10
    else:
        print(f"{name} fails to catch the bird and watches it fly away, alerting the other prey in the area.")
        return -5


def rival_battle(name, stats, special_ability):
    #Scenario 2 features a battle with a rival clan member! Use stats and unique abilities wisely to defeat the opponent.
    """Scenario 2: Rival battle."""
    print("\nScenario 2: Rival Battle")
    rival_name = random.choice(["Shiver-paw", "Tiger-claw", "Leaf-paw"])
    rival_stats = {
        "Strength": random.randint(5, 15),
        "Agility": random.randint(5, 15),
        "Intelligence": random.randint(5, 15),
    }
    print(f"A rival cat, {rival_name}, charges at you during battle!")
    print(f"Rival Stats: {rival_stats}")
    print("1. Fight back! (Strength needed)")
    print("2. Use your brain to strategize necessary attacks. (Intelligence needed)")
    print("3. Utilize unique ability. (Unique ability is used)")

    choice = input("Choose your strategy (1/2/3): ")
    if choice == "1" and stats["Strength"] > rival_stats["Strength"]:
        print(f"{name} defeats {rival_name} in battle! Nice job!")
        return 15
    elif choice == "2" and stats["Intelligence"] > rival_stats["Intelligence"]:
        print(f"{name} outsmarts {rival_name} and wins! Awesome!")
        return 15
    elif choice == "3":
        if special_ability == "Extra Strength":
            print(f"{name} uses Extra Strength to seriously do some damage to {rival_name}. The opponent scampers off!")
            return 15
        elif special_ability == "Healing":
            print(f"{name} feels the adrenaline come through and recovers quick to successfully defeat {rival_name}!")
            return 15
        else:
            print(f"{name} escapes by disappearing into the trees. The opponent looks around confusedly. Nice job!")
            return 15
    else:
        print(f"{name} is defeated by {rival_name}. {name} runs back to camp, injured!")
        return -10


def stealth_escape(name, stats, special_ability):
    #Scenario 3--your character must choose how they confront a dangerous animal during their hunt! stealth ability can be utilized for this scenario.
    """Scenario 3: You encounter a dangerous animal while hunting!"""
    print("\nScenario 3: Dangerous encounter")
    print("You find yourself face to face with a badger!")
    print("1. Fight back! (Strength needed)")
    print("2. Use your smaller size to your advantage and escape! (Intelligence needed)")
    print("3. Use your unique ability. (Unique ability utilized)")

    choice = input("What do you do? (1/2/3): ")
    if choice == "1" and stats["Strength"] > 12:
        print(f"{name} claws the badger's eyes and escape when it turns tail and runs! Nice!")
        return 10
    elif choice == "2" and stats["Intelligence"] > 12:
        print(f"{name} uses their smaller size to dodge the badger's attack and escape! Success!")
        return 10
    elif choice == "3":
        if special_ability == "Stealth":
            print(f"{name} uses their stealth to escape without a trace!")
            return 10
        else:
            print(f"{name}'s unique ability isn't useful here.")
            return -5
    else:
        print(f"{name} is roughed up by the badger and scampers off to camp after escaping with critical injuries. Try again.")
        return -10

if __name__ == "__main__":
    main()
