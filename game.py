import random
import sys

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

    def heal(self, gained_hp):
        """increases hp"""
        self.hp += gained_hp

class Vampire(object):
    """defines a vampire"""

    def __init__(self, hp):
        """health of vampire"""
        self.hp = hp

    def damage(self, lost_hp):
        """decreases hp"""
        self.hp -= lost_hp

buffy = Character("Buffy", "Summers",
"vampire slayer and student at Sunnydale High who is best friends with Willow and Xander",
"super strength, super healing, and fighting abilities",
"peppy but brave and strong", 30)

willow = Character("Willow", "Rosenberg",
"witch, hacker, and student at Sunnydale High who is best friends with Buffy and Xander",
"magic ability, hacking skills, and intelligence",
"shy, sweet and very smart", 30)

xander = Character("Xander", "Harris",
"student at Sunnydale High who is best friends with Buffy and Willow",
"creativity and ingenuity",
"brave and loyal to his friends", 30)

giles = Character("Rupert", "Giles",
"librarian at Sunnydale High and Buffy's mentor",
"knowledge and magic ability",
"British, bookish, and a father-figure to the others", 30)

def keep_going():
    """prints user input"""
    print(input("[ENTER]"))

list_of_protagonists = [buffy, willow, xander, giles]

for character in list_of_protagonists:
    character.describe()
    keep_going()

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
You're in the library with {other_scoobies}. There is a coven of evil witches coming to Sunnydale to do a spell to end the world. You need to research to find out what spells they're going to use and how to stop them. Which book do you want to read first?""")
keep_going()
print("1. Demons and Witches Through the Ages")
print("2. The Darkest Magicks")
print("3. Watcher's Journal 1899-1903")
print("4. Spellcasting for Dummies")

choice = int(input("Type the number of your choice. "))

while choice != 3:
    if choice == 1:
        print("""You read the book and learn a lot about the various ways demons can disembowel people, and the evolution of witchcraft during the Salem Witch Trials. It is excruciatingly boring and you learn nothing about apocalypse spells.""")
        keep_going()
    elif choice == 2:
        print("""When you open the book, there's a strange sound. Suddenly, the book bursts into flames. Then, everything is on fire. This is why you don't mess with the dark arts! You burn to death slowly.

        GAME OVER""")
        sys.exit()
    elif choice == 4:
        print("""You read about the basics of spellcasting: how to make a pencil fly or sparks appear. The book explains in mind-numbing detail every step of every spell. You can barely keep your eyes open and have learned nothing worthwhile.""")
        keep_going()
    else:
        print("That's not one of the books. Try again.")
    choice = int(input("Type the number of your choice. "))

not_dead = "false"
user_choice = 0
if choice == 3:
    print("""You find that the Watcher has faced this coven years ago. She writes that to stop the spell, you need to collect:
        Salamander eyes
        Orb of Ramjarin
        Doll's Eye Crystal""")
    not_dead = "yay"
    keep_going()

inventory = []

places = """
1. Magic Shop
2. Restfield Cemetery
3. Catacombs
4. The Hellmouth"""


if not_dead == "yay":
    print(f"""
    Where would you like to go?
    {places}""")
    user_choice = int(input("Type the number of your choice. "))

magic_shop_choices = """Do you want to:
    1. Look for salamander eyes
    2. Ask about the Orb of Ramjarin
    3. Talk to the owner of the shop
    4. Ask about Ghora demons
    5. View inventory
    6. Leave"""

for x in range(10000):
    while user_choice == 1:
        print(f"""At the Magic Shop, you see shelves full of ingredients. {magic_shop_choices}""")
        answer = int(input("Type the number of your choice. "))
        if answer == 1:
            print("""You find salamander eyes on a shelf in the back! However, when you go to pay for them, you realize you left your money at home :(. You ask the owner if there is any way you can get the eyes now, and she says she'll give them to you for free if you answer the following riddle:

            What happens one in a month, twice in a moment, and never in a thousand years?""")
            keep_going()
            riddle_response = input("Type your response: ")
            if riddle_response == 'm' or riddle_response == 'M' or riddle_response == 'the letter m':
                if "salamander eyes" not in inventory:
                    inventory.append("salamander eyes")
                print("You got the salamander eyes! They have been added to your inventory.")
            else:
                print("Sorry, that's incorrect. Come back later and try again.")
            keep_going()

        if answer == 2:
            print("""You ask if she knows where to get an Orb of Ramjarin, and she replies, 'Well, I heard a gang of vampires in the cemetery were talking about getting one.'""")
            keep_going()

        if answer == 3:
            print("""You ask how the owner's day has been. She is offended by your impertinence, and suddenly her skin peels away to reveal a montrous demon. The demon rips your head off. Oops.

            GAME OVER""")
            sys.exit()

        if answer == 4:
            print("""You ask about Ghora demons, and the shop owner says, 'Funny you should ask...' Suddenly, her skin peels away to reveal a monstrous demon. The demon rips your head off. Oops

            GAME OVER'""")
            sys.exit()

        if answer == 5:
            print(inventory)
            keep_going()

        if answer == 6:
            print(f"Where would you like to go? {places}")
            keep_going()
            user_choice = int(input("Type the number of your choice. "))

    while user_choice == 2:
        vamp1 = Vampire(20)
        print("""
        You arrive at the cemetery. It is dark and creepy, and you feel uneasy. Suddenly, you see a vampire lurking in the dark! What do you do?
        1. Run away
        2. Fight
        3. Beg for mercy""")
        answer = int(input("Type the number of your choice. "))

        if answer == 1:
            if user_character == xander:
                print("""You run as fast as you can, and hide behind some tombstones. The vampire chasing you trips and falls right on a branch and turns to dust. What an idiot. All that is left is a silvery orb. The Orb of Ramjarin! You grab it.""")
                inventory.append("Orb of Ramjarin")
                print(f"""
                Where would you like to go?
                {places}""")
                keep_going()
                user_choice = int(input("Type the number of your choice. "))

            else:
                print("""You try to run, but the vampire is faster. You trip over an inconveniently placed tombstone and fall to the ground. The vampire snaps your neck.

                GAME OVER""")
                sys.exit()

        if answer == 2:
            cemetery_choices = """What would you like to do?
                1. Stake vamp
                2. Punch vamp
                3. Use sword"""
            if user_character == buffy:
                print(f"""
                You're a Vampire Slayer! Of course you're going to fight. You have {buffy.hp} health.""")
                keep_going()
                answer = int(input(f"""{cemetery_choices}

                Type the number of your choice. """))

                status = 'fighting'
                while status == 'fighting':
                    while answer == 1:
                        odds = random.randint(1, 20)
                        if odds in range(1, 8):
                            buffy.damage(random.randint(1,5))
                            if buffy.hp > 0:
                                print(f"""
                                You miss. The vampire still has {vamp1.hp} health, and he manages to hit you. You now have {buffy.hp} health.""")
                                keep_going()
                                answer = int(input(f"""{cemetery_choices}

                                Type the number of your choice. """))
                            else:
                                answer = "dead :("
                                print("""
                                The vampire was too strong, and killed you. RIP :(

                                GAME OVER""")
                                sys.exit()

                        elif odds in range(9, 19):
                            vamp1.damage(random.randint(3, 7))
                            if vamp1.hp > 0:
                                print(f"""
                                You hit the vampire, but miss his heart. He now has {vamp1.hp} health.""")
                                keep_going()
                                answer = int(input(f"""{cemetery_choices}

                                Type the number of your choice. """))

                            else:
                                answer = "ur outta here"
                                print(f"""
                                You kill the vampire! He turns to dust, leaving behind only a silvery orb. The Orb of Ramjarin! You grab it. One step closer to beating those witches!""")
                                inventory.append("Orb of Ramjarin")
                                status = 'done'
                                if buffy.hp <= 25:
                                    buffy.heal(5)
                                else:
                                    buffy.hp = 30
                                keep_going()
                                print(f"""
                                Where would you like to go?
                                {places}""")
                                user_choice = int(input("Type the number of your choice. "))

                        elif odds == 20:
                            answer = "ur outta here"
                            vamp1.hp = 0
                            print(f"""
                            You kill the vampire! He turns to dust, leaving behind only a silvery orb. The Orb of Ramjarin! You grab it. One step closer to beating those witches!""")
                            inventory.append("Orb of Ramjarin")
                            status = 'done'
                            if buffy.hp <= 25:
                                buffy.heal(5)
                            else:
                                buffy.hp = 30
                            keep_going()
                            print(f"""Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))

                    while answer == 2:
                        odds = random.randint(1, 10)
                        if odds in range(1, 3):
                            buffy.damage(random.randint(2, 4))
                            if buffy.hp > 0:
                                print(f"""
                                You miss, stumble over a hidden root, and fall down. Darn your clumsiness! The vampire takes this opportunity to kick you in the ribs. Ouch. You now have {buffy.hp} health.""")
                                keep_going()
                                answer = int(input(f"""{cemetery_choices}

                                Type the number of your choice. """))
                            else:
                                print("""
                                You miss completely and fall down. The vampire wastes no time in snapping your neck. RIP :(

                                GAME OVER""")
                                sys.exit()

                        elif odds in range(4, 7):
                            buffy.damage(random.randint(1, 2))
                            vamp1.damage(random.randint(2, 4))
                            if buffy.hp > 0 and vamp1.hp > 0:
                                print(f"""
                                You land a hit on the vamp, but lose your footing. He catches you in the jaw with a nasty punch. You now have {buffy.hp} health and he has {vamp1.hp} health.""")
                                keep_going()
                                answer = int(input(f"""{cemetery_choices}

                                Type the number of your choice. """))
                            elif buffy.hp > 0 and vamp1.hp <= 0:
                                answer = "ur outta here"
                                print(f"""
                                The vampire manages to get a hit in, but you hit him with a flurry of punches and he falls down, turning to dust. All that is left is a silvery orb. The Orb of Ramjarin! You have {buffy.hp} health.""")
                                inventory.append("Orb of Ramjarin")
                                status = 'done'
                                if buffy.hp <= 25:
                                    buffy.heal(5)
                                else:
                                    buffy.hp = 30
                                keep_going()
                                print(f"""
                                Where would you like to go?
                                {places}""")
                                user_choice = int(input("Type the number of your choice. "))

                        else:
                            vamp1.damage(random.randint(3, 5))
                            if vamp1.hp > 0:
                                print(f"""
                                You land a solid hit on the vampire! He falls down, and you take the opportunity to crack a brilliant pun. He now has {vamp1.hp} health.""")
                                keep_going()
                                answer = int(input(f"""{cemetery_choices}

                                Type the number of your choice. """))
                            else:
                                answer = "ur outta here"
                                print(f"""
                                The vampire manages to get a hit in, but you hit him with a flurry of punches and he falls down, turning to dust. All that is left is a silvery orb. The Orb of Ramjarin! You have {buffy.hp} health.""")
                                inventory.append("Orb of Ramjarin")
                                status = 'done'
                                if buffy.hp <= 25:
                                    buffy.heal(5)
                                else:
                                    buffy.hp = 30
                                keep_going()
                                print(f"""
                                Where would you like to go?
                                {places}""")
                                user_choice = int(input("Type the number of your choice. "))

                    while answer == 3:
                        odds = random.randint(1, 20)
                        if odds in range(1, 8):
                            buffy.damage(random.randint(1,5))
                            if buffy.hp > 0:
                                print(f"""
                                You aim too high. The vampire still has {vamp1.hp} health, and he manages to land a hit. You now have {buffy.hp} health.""")
                                keep_going()
                                answer = int(input(f"""{cemetery_choices}

                                Type the number of your choice. """))
                            else:
                                answer = "dead :("
                                print("""
                                The vampire knocked the sword out of your hand and killed you. RIP :(

                                GAME OVER""")

                        elif odds in range(9, 19):
                            vamp1.damage(random.randint(3, 7))
                            if vamp1.hp > 0:
                                print(f"""
                                You stab the vampire, but miss his heart. Also, now your sword is stuck in his chest. He now has {vamp1.hp} health.""")
                                keep_going()
                                answer = int(input(f"""{cemetery_choices}

                                Type the number of your choice. """))

                            else:
                                answer = "ur outta here"
                                print(f"""
                                You decapitate the vampire! He turns to dust, leaving behind only a silvery orb. The Orb of Ramjarin! You grab it. One step closer to beating those witches!""")
                                inventory.append("Orb of Ramjarin")
                                status = 'done'
                                if buffy.hp <= 25:
                                    buffy.heal(5)
                                else:
                                    buffy.hp = 30
                                keep_going()
                                print(f"""
                                Where would you like to go?
                                {places}""")
                                user_choice = int(input("Type the number of your choice. "))

                        elif odds == 20:
                            answer = "ur outta here"
                            vamp1.hp = 0
                            print(f"""
                            You decapitate the vampire! He turns to dust, leaving behind only a silvery orb. The Orb of Ramjarin! You grab it. One step closer to beating those witches!""")
                            inventory.append("Orb of Ramjarin")
                            status = 'done'
                            if buffy.hp <= 25:
                                buffy.heal(5)
                            else:
                                buffy.hp = 30
                            keep_going()
                            print(f"""
                            Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))

            elif user_character == willow:
                print(f"""
                You decide to stand your ground and fight. What would you like to do?
                1. Magic spell to summon fire
                2. Stake vampire
                3. Run away""")
                answer = int(input("Type the number of your choice. "))

                if answer == 1:
                    magic_choice = int(input("""
                    You scramble to find the ingredients for your spell. You have aspen bark, sage, thyme, and a rose quartz crystal. Which do you use?
                    1. aspen bark and sage
                    2. thyme and the crystal

                    Type the number of your choice: """))
                    if magic_choice == 1:
                        print("""You say the incantation, but end up lighting yourself on fire! You probably should've practiced a bit more...

                        GAME OVER""")
                        sys.exit()
                    if magic_choice == 2:
                        print("""The spell works! The vampire catches fire and burns quickly to dust, leaving behind only a silvery orb. The Orb of Ramjarin! You quickly grab it""")
                        inventory.append("Orb of Ramjarin")
                        keep_going()
                        print(f"""Where would you like to go?
                        {places}""")
                        user_choice = int(input("Type the number of your choice. "))

                elif answer == 2:
                    print("""You try to fight, but the vampire is supernaturally strong, and you only have human strength. It snaps your neck. RIP.

                    GAME OVER""")
                    sys.exit()

                elif answer == 3:
                    print("""You try to run, but the vampire is faster. You trip over an inconveniently placed tombstone and fall to the ground. The vampire snaps your neck.

                    GAME OVER""")
                    sys.exit()

            elif user_character == xander:
                print("""You try to fight, but the vampire is supernaturally strong, and you're just a human. It snaps your neck. RIP.

                GAME OVER""")
                sys.exit()

            elif user_character == giles:
                print(f"""
                You decide to stand your ground and fight. What would you like to do?
                1. Magic spell to summon fire
                2. Stake vampire
                3. Run away""")
                answer = int(input("Type the number of your choice. "))

                if answer == 1:
                    magic_choice = int(input("""
                    You scramble to find the ingredients for your spell. You have aspen bark, sage, thyme, and a rose quartz crystal. Which do you use?
                    1. aspen bark and sage
                    2. thyme and the crystal

                    Type the number of your choice: """))
                    if magic_choice == 1:
                        print("""You say the incantation, but end up lighting yourself on fire! You probably should've practiced a bit more...

                        GAME OVER""")
                        sys.exit()
                    if magic_choice == 2:
                        print("""The spell works! The vampire catches fire and burns quickly to dust, leaving behind only a silvery orb. The Orb of Ramjarin! You quickly grab it""")
                        inventory.append("Orb of Ramjarin")
                        keep_going()
                        print(f"""
                        Where would you like to go?
                        {places}""")
                        user_choice = int(input("Type the number of your choice. "))

                elif answer == 2:
                    print("""You try to fight, but the vampire is supernaturally strong, and you only have human strength. It snaps your neck. RIP.

                    GAME OVER""")
                    sys.exit()

                elif answer == 3:
                    print("""You try to run, but the vampire is faster. You trip over an inconveniently placed tombstone and fall to the ground. The vampire snaps your neck.

                    GAME OVER""")
                    sys.exit()

        if answer == 3:
            print("""You plead with the vampire not to hurt you, but he doesn't care. He's evil, remember? You die horribly.

            GAME OVER""")
            sys.exit()

    while user_choice == 3:
        print("""You arrive at the catacombs, where it's dark and creepy. It feels like something's watching you... There are two tunnels disappearing into the gloom. Which one do you pick?
        1. Right tunnel
        2. Left tunnel
        """)
        user_input = int(input("Type the number of your choice. "))
        if user_input == 1:
            if user_character == buffy:
                print("""
                You see a shadowy figure ahead of you. You creep closer and see the silhouette of a creature that is clearly not human and carrying a wickedly sharp sword. There's a glowing crystal around his neck. What do you do?
                1. Run away
                2. Fight the demon
                """)
                buffy_answer = int(input("Type the number of your choice. "))
                if buffy_answer == 1:
                    print(f"""
                    Where would you like to go?
                    {places}""")
                    user_choice = int(input("Type the number of your choice. "))

                elif buffy_answer == 2:
                    buffy_answer2 = int(input("""
                    Do you want to:
                    1. Creep up behind the demon
                    2. Attack from the front

                    Type the number of your choice. """))
                    if buffy_answer2 == 1:
                        buffy_answer3 = int(input("""
                        You sneak up behind the demon, and manage to surprise him. While he is reeling back in shock, you pull out the stake you always keep handy and stab him in the heart, and he falls down dead. What do you want to do now?
                        1. Get out of there
                        2. Check out the weird glowing crystal

                        Type the number of your choice. """))
                        if buffy_answer3 == 1:
                            print(f"""
                            Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))
                        elif buffy_answer3 == 2:
                            print("""
                            You grab the crystal to examine it, and it looks just like the picture of a doll's eye crystal! Now you're one step closer to defeating the evil witches.""")
                            inventory.append("doll's eye crystal""")
                            keep_going()
                            print(f"""Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))
                    elif buffy_answer2 == 2:
                        print("""
                        You run at the demon, yelling a battle cry, but he can see far better than you in the dark, and he uses his sword to chop your head off. RIP.

                        GAME OVER""")
                        sys.exit()

            if user_character == willow:
                print("""You see a shadowy figure ahead of you. You creep closer and see the silhouette of a creature that is clearly not human and carrying a wickedly sharp sword. There's a glowing crystal around his neck. What do you do?
                1. Run away
                2. Fight the demon
                """)
                willow_answer = int(input("Type the number of your choice. "))
                if willow_answer == 1:
                    print(f"""
                    Where would you like to go?
                    {places}""")
                    user_choice = int(input("Type the number of your choice. "))

                elif willow_answer == 2:
                    willow_answer2 = int(input("""
                    You remember that the demon has a weakness for either ice or fire, but you can't remember which one. Do you want to:
                    1. Do a magic spell to summon fire
                    2. Do a magic spell to summon ice

                    Type the number of your choice. """))
                    if willow_answer2 == 1:
                        print("""
                        You hastily say the incantation to summon fire, and the demon catches on fire. But he doesn't die, in fact, he seems to be getting stronger... He reaches out to grab you, and suddenly you're on fire. Uh oh...

                        GAME OVER""")
                        sys.exit()
                    elif willow_answer2 == 2:
                        willow_answer3 = int(input("""
                        You hastily say the incantation to summon ice, and the demon freezes over, ice creeping up his limbs before shattering into a million pieces. You chose correctly! What do you want to do now?
                        1. Get out of there
                        2. Check out the weird glowing crystal

                        Type the number of your choice. """))
                        if willow_answer3 == 1:
                            print(f"""
                            Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))
                        elif willow_answer3 == 2:
                            print("""
                            You grab the crystal to examine it, and it looks just like the picture of a doll's eye crystal! Now you're one step closer to defeating the evil witches.""")
                            inventory.append("doll's eye crystal""")
                            keep_going()
                            print(f"""Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))

            if user_character == xander:
                print("""You see a shadowy figure ahead of you. You creep closer and see the silhouette of a creature that is clearly not human and carrying a wickedly sharp sword. There's a glowing crystal around his neck. What do you do?
                1. Run away
                2. Try to outsmart the demon
                """)
                xander_answer = int(input("Type the number of your choice. "))
                if xander_answer == 1:
                    print(f"""
                    Where would you like to go?
                    {places}""")
                    user_choice = int(input("Type the number of your choice. "))

                elif xander_answer == 2:
                    xander_answer2 = int(input("""
                    You vaguely remember that the demon is afraid of either bunnies or kittens, but you can't remember which one. Do you want to:
                    1. Scare the demon with bunnies
                    2. Scare the demon with kittens

                    Type the number of your choice. """))
                    if xander_answer2 == 1:
                        xander_answer3 = int(input("""
                        You yell that an army of bunnies are hopping down into the catacombs, and the demons screams in a strangely high-pitched voice and runs away, leaving his sword and glowing crystal behind. You chose correctly! What do you want to do now?
                        1. Get out of there
                        2. Check out the weird glowing crystal

                        Type the number of your choice. """))
                        if xander_answer3 == 1:
                            print(f"""
                            Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))
                        elif xander_answer3 == 2:
                            print("""
                            You grab the crystal to examine it, and it looks just like the picture of a doll's eye crystal! Now you're one step closer to defeating the evil witches.""")
                            inventory.append("doll's eye crystal""")
                            keep_going()
                            print(f"""Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))
                    elif xander_answer2 == 2:
                        print("""
                        You yell that an army of kittens is coming, and the demons bursts out laughing. 'Was that supposed to scare me?' he asks. Then his rips your head off.

                        GAME OVER""")
                        sys.exit()

            if user_character == giles:
                print("""You see a shadowy figure ahead of you. You creep closer and see the silhouette of a creature that is clearly not human and carrying a wickedly sharp sword. There's a glowing crystal around his neck. What do you do?
                1. Run away
                2. Fight the demon
                """)
                giles_answer = int(input("Type the number of your choice. "))
                if giles_answer == 1:
                    print(f"""
                    Where would you like to go?
                    {places}""")
                    user_choice = int(input("Type the number of your choice. "))

                elif giles_answer == 2:
                    giles_answer2 = int(input("""
                    You remember that the demon has a weakness for either ice or fire, but you can't remember which one. Do you want to:
                    1. Do a magic spell to summon fire
                    2. Do a magic spell to summon ice

                    Type the number of your choice. """))
                    if giles_answer2 == 1:
                        print("""
                        You hastily say the incantation to summon fire, and the demon catches on fire. But he doesn't die, in fact, he seems to be getting stronger... He reaches out to grab you, and suddenly you're on fire. Uh oh...

                        GAME OVER""")
                        sys.exit()
                    elif giles_answer2 == 2:
                        giles_answer3 = int(input("""
                        You hastily say the incantation to summon ice, and the demon freezes over, ice creeping up his limbs before shattering into a million pieces. You chose correctly! What do you want to do now?
                        1. Get out of there
                        2. Check out the weird glowing crystal

                        Type the number of your choice. """))
                        if giles_answer3 == 1:
                            print(f"""
                            Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))
                        elif giles_answer3 == 2:
                            print("""
                            You grab the crystal to examine it, and it looks just like the picture of a doll's eye crystal! Now you're one step closer to defeating the evil witches.""")
                            inventory.append("doll's eye crystal""")
                            keep_going()
                            print(f"""Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))

        if user_input == 2:
            print("""You walk carefully into the dark tunnel. It just gets darker and darker, until you can't see anything at all. Then, suddenly, the ground beneath your feet disappears. Uh oh...

            GAME OVER""")
            sys.exit()


    while user_choice == 4:
        print("""
        You arrive at the Hellmouth, and see three shadowy figures standing in a circle and chanting. The witches! They don't seem to notice you, but they will soon. If you have the items to stop them, now is your chance to use them. What do you do?
        1. Try to stop the witches
        2. Leave""")
        answer = int(input("Type the number of your choice. "))
        if answer == 1:
            if "salamander eyes" in inventory and  "Orb of Ramjarin" in inventory and "doll's eye crystal" in inventory:
                print("""You quickly assemble the ingredients and carefully say the incantation. The room fills with blinding light, and you have to close your eyes. When you open them, the witches are nowhere to be found. You did it!

                YOU SAVED THE WORLD! YAY!""")
                sys.exit()
            else:
                print("""
                You scramble to assemble the ingredients, and suddenly realize you don't have them all. Suddenly, the witches turn. They've spotted you. The last thing you see is their glowing red eyes. At least you won't be around to witness the end of the world...

                GAME OVER""")
                sys.exit()

        if answer == 2:
            print(f"""
            Where would you like to go?
            {places}""")
            user_choice = int(input("Type the number of your choice. "))











