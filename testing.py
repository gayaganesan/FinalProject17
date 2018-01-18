import random

class Character(object):
    """defines a character"""

    def __init__(self, firstname, lastname, job, abilities, personality, hp):
        """atributes of character"""
        self.firstname = firstname
        self.lastname = lastname
        self.job = job
        self.abilities = abilities
        self.personality = personality
        self.hp = hp

    def describe(self):
        """prints description of character"""
        print(f"""
        {self.firstname} {self.lastname} is {self.personality}. {self.firstname} is a {self.job}. {self.firstname} has {self.abilities}.""")

    def damage(self, lost_hp):
        """decreases hp"""
        self.hp -= lost_hp

buffy = Character("Buffy", "Summers",
"vampire slayer and student at Sunnydale High who is best friends with Willow and Xander",
"super strength, super healing, and fighting abilities",
"peppy but brave and strong", 30)

user_character = buffy

places = """1. Magic Shop
2. Restfield Cemetery
3. Catacombs"""

user_choice = 4

inventory = ["salamander eyes", "Orb of Ramjarin", "doll's eye crystal"]

if user_choice == 4:
    print("""You arrive at the Hellmouth, and see three shadowy figures standing in a circle and chanting. The witches! They don't seem
    to notice you, but they will soon. If you have the items to stop them, now is your chance to use them. What do you do?
    1. Try to stop the witches
    2. Leave""")
    answer = int(input("Type the number of your choice. "))
    if answer == 1:
        if "salamander eyes" in inventory and  "Orb of Ramjarin" in inventory and "doll's eye crystal" in inventory:
            print("""WIN FILLER""")
        else:
            print("""LOSE FILLER""")

    if answer == 2:
        print(f"""Where would you like to go?
        {places}""")
        user_choice = int(input("Type the number of your choice. "))