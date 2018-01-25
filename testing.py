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

user_choice = 3

inventory = ["salamander eyes", "Orb of Ramjarin"]

while user_choice == 3:
        print("""You arrive at the catacombs, where it's dark and creepy. It feels like something's watching you... There are three tunnels
        disappearing into the gloom. Which one do you pick?
        1. Right tunnel
        2. Center tunnel
        3. Left tunnel
        """)
        user_input = int(input("Type the number of your choice. "))
        if user_input == 1:
            if user_character == buffy:
                print("""You see a shadowy figure ahead of you. You creep closer and see the silhouette of a creature that is clearly not human and
                carrying a wickedly sharp sword. There's a glowing crystal around his neck. What do you do?
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
                        You sneak up behind the demon, and manage to surprise him. While he is reeling back in shock, you pull out the stake you
                        always keep handy and stab him in the heart, and he falls down dead. What do you want to do now?
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
                            You grab the crystal to examine it, and it looks just like the picture of a doll's eye crystal! Now you're one step closer
                            to defeating the evil witches.""")
                            inventory.append("doll's eye crystal""")
                            print(f"""
                            Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))
                    elif buffy_answer2 == 2:
                        print("""
                        You run at the demon, yelling a battle cry, but he can see far better than you in the dark, and he uses his sword
                        to chop your head off. RIP.

                        GAME OVER""")
                        break

            if user_character == willow:
                print("""You see a shadowy figure ahead of you. You creep closer and see the silhouette of a creature that is clearly not human and
                carrying a wickedly sharp sword. There's a glowing crystal around his neck. What do you do?
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
                        You hastily say the incantation to summon fire, and the demon catches on fire. But he doesn't die, in fact, he seems to be getting stronger...
                        He reaches out to grab you, and suddenly you're on fire. Uh oh...

                        GAME OVER""")
                        break
                    elif willow_answer2 == 2:
                        willow_answer3 = int(input("""
                        You hastily say the incantation to summon ice, and the demon freezes over, ice creeping up his limbs before shattering into a million pieces
                        You chose correctly! What do you want to do now?
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
                            You grab the crystal to examine it, and it looks just like the picture of a doll's eye crystal! Now you're one step closer
                            to defeating the evil witches.""")
                            inventory.append("doll's eye crystal""")
                            print(f"""
                            Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))

            if user_character == xander:
                print("""You see a shadowy figure ahead of you. You creep closer and see the silhouette of a creature that is clearly not human and
                carrying a wickedly sharp sword. There's a glowing crystal around his neck. What do you do?
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
                        You yell that an army of bunnies are hopping down into the catacombs, and the demons screams in a strangely high-pitched voice and runs
                        away, leaving his sword and glowing crystal behind. You chose correctly! What do you want to do now?
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
                            You grab the crystal to examine it, and it looks just like the picture of a doll's eye crystal! Now you're one step closer
                            to defeating the evil witches.""")
                            inventory.append("doll's eye crystal""")
                            print(f"""
                            Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))
                    elif xander_answer2 == 2:
                        print("""
                        You yell that an army of kittens is coming, and the demons bursts out laughing. 'Was that supposed to scare me?' he asks. Then his rips your head off.

                        GAME OVER""")
                        break

            if user_character == giles:
                print("""You see a shadowy figure ahead of you. You creep closer and see the silhouette of a creature that is clearly not human and
                carrying a wickedly sharp sword. There's a glowing crystal around his neck. What do you do?
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
                        You hastily say the incantation to summon fire, and the demon catches on fire. But he doesn't die, in fact, he seems to be getting stronger...
                        He reaches out to grab you, and suddenly you're on fire. Uh oh...

                        GAME OVER""")
                        break
                    elif giles_answer2 == 2:
                        giles_answer3 = int(input("""
                        You hastily say the incantation to summon ice, and the demon freezes over, ice creeping up his limbs before shattering into a million pieces
                        You chose correctly! What do you want to do now?
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
                            You grab the crystal to examine it, and it looks just like the picture of a doll's eye crystal! Now you're one step closer
                            to defeating the evil witches.""")
                            inventory.append("doll's eye crystal""")
                            print(f"""
                            Where would you like to go?
                            {places}""")
                            user_choice = int(input("Type the number of your choice. "))