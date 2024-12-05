import random
import cowsay
import pyfiglet
from tkinter import Tk, Label
from PIL import Image, ImageTk, ImageDraw, ImageFont


def render_text(text, font="digital"):
    return pyfiglet.figlet_format(text, font=font)


def create_cat():
    # Create a cat character in the warriors universe beginning with the suffix -paw to symbolize apprenticeship
    cowsay.kitty("Welcome to a Warrior Cats text-based adventure game!")
    print("Let's get our character started.\n")
    prefix = input("Choose a nature-based prefix! (Leaf, Snow, Fire, Ice, etc.):")
    name = prefix + "-paw"
    clan = input(f"What clan does {name} choose?")

    # Create randomized stats including strength, agility, and intelligence.
    stats = {
        "Strength": random.randint(5, 15),
        "Intelligence": random.randint(5, 15),
        "Agility": random.randint(5, 15),
    }

    print(render_text(f"{name} of {clan}", font="digital"))

    # Cats will have a unique ability that they can utilize during certain scenarios.
    print("\nChoose a unique ability:")
    print("1. Healing (Heal if points are lost after battles)")
    print("2. Extra Strength (Does more damage during a battle scenario)")
    print("3. Stealth (Ability to escape danger)")
    ability = input("What will be your unique ability? (1/2/3): ")
    abilities = {1: "Healing", 2: "Extra Strength", 3: "Stealth"}
    special_ability = abilities.get(int(ability), "Healing")

    print((f"\n{name} of {clan} has chosen {special_ability}!"))
    print((f"Stats: {stats}\n"))
    return name, clan, stats, special_ability


def replace_suffix(name):
    suffixes = ["dapple", "tail", "pelt", "fur", "nose", "flight", "song", "fur"]
    return name.split("-")[0] + f"-{random.choice(suffixes)}"


def upgrade_to_warrior(name, stats, successful_scenarios):
    if successful_scenarios >= 2:    
        name = replace_suffix(name)
        print(f"\n{name} has earned their warrior name!")
    return name


def hunting_scenario(name, stats):
    print(("Scenario 1: Hunting"))
    print(("You spot a bird on a branch--it looks like it is foraging for something. You think about what you should do."))
    print(("1. You stealthily scale up the tree and try to catch it silently (Agility needed)"))
    print(("2. You wait for it to leap down to continue its forage, and then you strike (Intelligence needed)"))
    print(("3. You leap upon the branch and catch it while it is off guard (Strength needed)"))

    choice = input("Choose an option (1/2/3): ")
    if choice == "1" and stats["Agility"] > 10:
        print((f"{name} sneakily climbs up and pounces on the bird. Nice!"))
        return 10
    elif choice == "2" and stats["Intelligence"] > 10:
        print((f"{name} patiently waits until the bird is on the ground and catches it. Success!"))
        return 10
    elif choice == "3" and stats["Strength"] > 10:
        print((f"{name} uses great force to leap up the tree and catch the bird in their jaws. Nice job!"))
        return 10
    else:
        print((f"{name} fails to catch the bird and watches it fly away, alerting the other prey in the area."))
        return -5


def rival_battle(name, stats, special_ability):
    print(("\nScenario 2: Rival Battle"))
    rival_name = random.choice(["Shiver-paw", "Tiger-claw", "Leaf-paw"])
    rival_stats = {
        "Strength": random.randint(5, 15),
        "Agility": random.randint(5, 15),
        "Intelligence": random.randint(5, 15),
    }
    print((f"A rival cat, {rival_name}, charges at you during battle!"))
    print((f"Rival Stats: {rival_stats}"))
    print(("1. Fight back! (Strength needed)"))
    print(("2. Use your brain to strategize necessary attacks. (Intelligence needed)"))
    print(("3. Utilize unique ability. (Unique ability is used)"))

    choice = input(("Choose your strategy (1/2/3): "))
    if choice == "1" and stats["Strength"] > rival_stats["Strength"]:
        print((f"{name} defeats {rival_name} in battle! Nice job!"))
        return 15
    elif choice == "2" and stats["Intelligence"] > rival_stats["Intelligence"]:
        print((f"{name} outsmarts {rival_name} and wins! Awesome!"))
        return 15
    elif choice == "3":
        if special_ability == "Extra Strength":
            print((f"{name} uses Extra Strength to seriously do some damage to {rival_name}. The opponent scampers off!"))
            return 15
        elif special_ability == "Healing":
            print((f"{name} feels the adrenaline come through and recovers quick to successfully defeat {rival_name}!"))
            return 15
        else:
            print((f"{name} escapes by disappearing into the trees. The opponent looks around confusedly. Nice job!"))
            return 15
    else:
        print((f"{name} is defeated by {rival_name}. {name} runs back to camp, injured!"))
        return -10


def stealth_escape(name, stats, special_ability):
    print(("\nScenario 3: Dangerous encounter"))
    print(("You find yourself face to face with a badger!"))
    print(("1. Fight back! (Strength needed)"))
    print(("2. Use your smaller size to your advantage and escape! (Intelligence needed)"))
    print(("3. Use your unique ability. (Unique ability utilized)"))

    choice = input("What do you do? (1/2/3): ")
    if choice == "1" and stats["Strength"] > 12:
        print((f"{name} claws the badger's eyes and escape when it turns tail and runs! Nice!"))
        return 10
    elif choice == "2" and stats["Intelligence"] > 12:
        print((f"{name} uses their smaller size to dodge the badger's attack and escape! Success!"))
        return 10
    elif choice == "3":
        if special_ability == "Stealth":
            print((f"{name} uses their stealth to escape without a trace!"))
            return 10
        else:
            print((f"{name}'s unique ability isn't useful here."))
            return -5
    else:
        print((f"{name} is roughed up by the badger and scampers off to camp after escaping with critical injuries. Try again."))
        return -10


def display_victory_image():
    image_path = r"C:\Users\ghost\proposalmd\src\cat.png"

    img = Image.open(image_path)

    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("CourierNew.ttf", 25) 
    except IOError:
        font = ImageFont.load_default()  

    text = "Congratulations! You are now a warrior cat!"
    text_position = (50, 50)
    text_color = (255, 255, 255) 

    draw.text(text_position, text, font=font, fill=text_color)

    root = Tk()
    root.title("Congratulations! You are now a warrior!")
    
    img_tk = ImageTk.PhotoImage(img)
    
    label = Label(root, image=img_tk)
    label.pack()

    root.mainloop()

def main():
    name, clan, stats, unique_ability = create_cat()

    successful_scenarios = 0

    if hunting_scenario(name, stats) > 0:
        successful_scenarios += 1
    if rival_battle(name, stats, unique_ability) > 0: 
        successful_scenarios += 1
    if stealth_escape(name, stats, unique_ability) > 0: 
        successful_scenarios += 1

    print(f"\nTotal successful scenarios: {successful_scenarios} out of 3")

    name = upgrade_to_warrior(name, stats, successful_scenarios)

    if successful_scenarios >= 2:
        print(f"Congratulations! {name} has become a warrior!")
        display_victory_image()  #Open the image in new window
    else:
        print(f"{name} has many moons ahead to yet become a warrior")


if __name__ == "__main__":
    main()