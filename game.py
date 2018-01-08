class Character(object):
    """defines a character"""

    def __init__(self, firstname, lastname, job, abilities, personality):
        """atributes of character"""
        self.firstname = firstname
        self.lastname = lastname
        self.job = job
        self.abilities = abilities
        self.personality = personality

    def describe(self):
        """prints description of character"""
        print(f"""
        {self.firstname} {self.lastname} is {self.personality}. {self.firstname} is a {self.job}. {self.firstname} has {self.abilities}.""")

buffy = Character("Buffy", "Summers",
"vampire slayer and student at Sunnydale High who is best friends with Willow and Xander",
"super strength, super healing, and fighting abilities",
"peppy but brave and strong")

willow = Character("Willow", "Rosenberg",
"witch, hacker, and student at Sunnydale High who is best friends with Buffy and Xander",
"magic ability, hacking skills, and intelligence",
"shy, sweet and very smart")

xander = Character("Xander", "Harris",
"student at Sunnydale High who is best friends with Buffy and Willow",
"creativity and ingenuity",
"brave and loyal to his friends")

giles = Character("Rupert", "Giles",
"librarian at Sunnydale High and Buffy's mentor",
"knowledge and magic ability",
"British, bookish, and a father-figure to the others")

list_of_protagonists = [buffy, willow, xander, giles]

for character in list_of_protagonists:
    character.describe()

def pick_character(protagonist):
    """lets user choose who they want to play as"""
    if protagonist.lower() == "buffy":
        user_character = buffy
        print(f"Nice choice! You picked {user_character.firstname} {user_character.lastname}")
    elif protagonist.lower() == "willow":
        user_character = willow
        print(f"Nice choice! You picked {user_character.firstname} {user_character.lastname}")
    elif protagonist.lower() == "xander":
        user_character = xander
        print(f"Nice choice! You picked {user_character.firstname} {user_character.lastname}")
    elif protagonist.lower() == "rupert":
        user_character = giles
        print(f"Nice choice! You picked {user_character.firstname} {user_character.lastname}")
    else:
        user_character = "Sorry, you don't have a character yet"
        print("Sorry, that's not a character here, try again!")
    return user_character

user_character = pick_character(input("Enter the first name of the character you want to play as. "))

while user_character == "Sorry, you don't have a character yet":
    user_character = pick_character(input("Enter the first name of the character you want to play as. "))

if user_character == buffy:
    other_scoobies = "Xander, Willow, and Giles"
elif user_character == willow:
    other_scoobies = "Buffy, Xander, and Giles"
elif user_character == xander:
    other_scoobies = "Buffy, Willow, and Giles"
else:
    other_scoobies = "Buffy, Willow, and Xander"

print(f"""
You're in the library with {other_scoobies}. There is a coven of evil witches coming to Sunnydale to do a
spell to end the world. You need to research to find out what spells they're going to use and how to stop
them. Which book do you want to read first?
1. Demons and Witches Through the Ages
2. The Darkest Magicks
3. Watcher's Journal 1899-1903
4. Spellcasting for Dummies""")

user_choice = int(input("Type the number of your choice. "))

while user_choice != 3:
    if user_choice == 1:
        print("""You read the book and learn a lot about the various ways demons can disembowel people, and the evolution of witchcraft
        during the Salem Witch Trials. It is excruciatingly boring and you learn nothing about apocalypse spells.""")
    elif user_choice == 2:
        print("""You learn about spells to flay people, spells to cause excruciating pain, spells to burn people alive, and spells to
        summon demons to do your bidding. It's mildly interesting, in a terrifying way, but there isn't anything that tells
        you how to *stop* the dark arts.""")
    elif user_choice == 4:
        print("""You read about the basics of spellcasting: how to make a pencil fly or sparks appear. The book explains in mind-numbing
        detail every step of every spell. You can barely keep your eyes open and have learned nothing worthwhile.""")
    else:
        print("That's not one of the books. Try again.")
    user_choice = int(input("Type the number of your choice. "))

if user_choice == 3:
    print("""You find that the Watcher has faced this coven years ago. She writes that to stop the spell, you need to collect""")




