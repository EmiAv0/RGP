class Player:
    def __init__(self,name,health,damage,strength,defense):
        self.name=name
        self.health = health
        self.damage = damage
        self.strength = strength
        self.defense = defense

    def damage_taken(self,damage):
        damage_taken = damage - self.defense
        self.health -= damage_taken
        return damage_taken

    def attack(self, target):
        damage = self.strength * 2
        damage_dealt = target.damage_taken(damage)
        return damage_dealt

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return self.health, self.damage, self.strength, self.defense

import random
import time

print("Welcome! Please choose your character name and stats below.")

character1=Player("",1002,102,102,102)
character1.name=input("Character's name: ")

while (character1.health >= 1001):
    print("Please pick a number 1-1000.")
    character1.health = input(character1.name + "'s health: ")
    character1.health = int(character1.health)

while (character1.damage > 101):
    print("Please pick a number 1-100.")
    character1.damage = input(character1.name + "'s damage: ")
    character1.damage = int(character1.damage)

while (character1.strength > 101):
    print("Please pick a number 1-100.")
    character1.strength = input(character1.name + "'s strength: ")
    character1.strength = int(character1.strength)

while (character1.defense > 101):
    print("Please pick a number 1-100.")
    character1.defense = input(character1.name + "'s defense: ")
    character1.defense = int(character1.defense)

print(" ")
character2 = Player("","","","","")
character2.name = input("Character name: ")

character2.health = random.randint(1,1000)
print(character2.name + "'s health: "+ str(character2.health))

character2.damage = random.randint(1,100)
print(character2.name + "'s damage: "+ str(character2.damage))

character2.strength = random.randint(1,100)
print(character2.name + "'s strength: "+ str(character2.strength))

character2.defense = random.randint(1,100)
print(character2.name + "'s defense: "+ str(character2.defense))

print(" ")
print(character1.name+" vs. "+character2.name)

while (character1.health > 0 and character2.health > 0):
    (character1.attack(character2))
    print(character1.name + " " + random.choice(
        ["assaults", "attacks", "strikes", "charges", "blitzes", "onslaughts", "volleys", "barrages", "bombards",
         "shells", "sieges", "pillages", "sacks", "plunders", "pushes", "ambushes", "surprises", "intercepts",
         "clashes", "combats", "battles", "fights", "scuffles", "melees", "brawls", "confronts", "contests", "injures",
         "harms", "wounds", "beats", "pummels", "thrashes", "flogs", "whips", "lashes", "stabs", "pierces", "impales",
         "hacks", "slashes", "cuts", "rips", "tears", "gouges", "scratches", "bites", "stings", "pecks", "claws",
         "pounces", "tackles", "charges", "rams", "slams", "smashes", "crushes", "destroys", "ravages", "devastates",
         "annihilates", "obliterates", 'wipes out']) + " " + character2.name + ". " + character2.name + "'s health is " + str(character2.health) + ".")

    time.sleep(0.5)
    (character2.attack(character1))
    print(character2.name + " " + random.choice(
        ["assaults", "attacks", "strikes", "charges", "blitzes", "onslaughts", "volleys", "barrages", "bombards",
         "shells", "sieges", "pillages", "sacks", "plunders", "pushes", "ambushes", "surprises", "intercepts",
         "clashes", "combats", "battles", "fights", "scuffles", "melees", "brawls", "confronts", "contests", "injures",
         "harms", "wounds", "beats", "pummels", "thrashes", "flogs", "whips", "lashes", "stabs", "pierces", "impales",
         "hacks", "slashes", "cuts", "rips", "tears", "gouges", "scratches", "bites", "stings", "pecks", "claws",
         "pounces", "tackles", "charges", "rams", "slams", "smashes", "crushes", "destroys", "ravages", "devastates",
         "annihilates", "obliterates", 'wipes out'])+" " + character1.name + ". " + character1.name + "'s health is " + str(character1.health) + ".")

    if (character1.health >= 0 and character2.health <= 0):
        print("K.0. " + character1.name + " wins." )

    if (character1.health <= 0 and character2.health >= 0):
        print("K.0. " + character2.name + " wins." )