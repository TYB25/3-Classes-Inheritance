import random
import time

print("Welcome to the Star Trek TOS vs TNG Fight Simulator")
print()

tos_tr: int = 0
tng_tr: int = 0
tng_ch: str = ""
tos_ch: str = ""
pl_ch: str = ""
mod_ch: str = ""

pick_chance = random.getrandbits(1)
side_boolean = bool(pick_chance)


def sel_list():
    print()
    print()
    print("Overall Selection:")
    print("TOS Crew: " + tos_ch)
    print("TNG Crew: " + tng_ch)
    print("Planet: " + pl_ch)
    print("Combat Selection: " + mod_ch)
    print()


class Crew:
    def __init__(self, name, position, actor, rank, base):
        self.name = name
        self.position = position
        self.rank = rank
        self.actor = actor
        self.base = base

    def att_list(self):
        print("Name- " + self.name)
        print("Rank- " + self.rank)
        print("Position- " + self.position)
        print("Actor- " + self.actor)
        print()


class tng_char(Crew):
    def __init__(self, name, position, actor, rank, base):
        super().__init__(name, position, actor, rank, base)


class Planet:
    def __init__(self, name, biome, base):
        self.name = name
        self.biome = biome
        self.base = base

    def plan_list(self):
        print("Name- " + self.name)
        print("Biome- " + self.biome)
        print()


class Mult:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def mult_list(self):
        print("Name- " + self.name)
        print("Description- " + self.description)
        print()


kirk = Crew("James Tiberius Kirk", "Captain", "William Shatner", "Captain", 20)
spock = Crew("Spock", "First Officer", "Leonard Nimoy", "Commander", 16)
mccoy = Crew("Leonard H. McCoy", "Physician", "DeForest Kelley", "Lieutenant Commander", 12)
scott = Crew("Montgomery Scott", "Engineer", "James Doohan", "Lieutenant Commander", 7)

picard = tng_char("Jean-Luc Picard", "Captain", "Patrick Stewart", "Captain", 15)
riker = tng_char("William Thomas Riker ", "First Officer", "Jonathan Frakes", "Commander", 12)
crush = tng_char("Beverly Cheryl Crusher", "Physician", "Gates McFadden", "Lieutenant Commander", 5)
worf = tng_char("Worf Rozhenko", "Chief Tactical Officer ", "Michael Dorn", "Lieutenant", 22)

earth = Planet("Earth (Starfleet Headquarters)", "Urban", 0)
cestus = Planet("Cestus III", "Desert", 10)
ent = Planet("USS Enterprise-D", "Starship", 10)
deneb = Planet("Deneb IV", "Grassland", 0)
deneb.base = random.randint(0, 20)

hand = Mult("Hand-to-hand combat", "Participants will fight without weapons", 0)
phase = Mult("Phaser combat", "Participants will fight using type 2 phasers", 0)
poly = Mult("Polywater intoxication", "Participants will have their inhibitions suppressed", 0)
man = Mult("Manual override", "Manually set final values (Debug)", 0)

print("Choice 1")
kirk.att_list()
print("Choice 2")
spock.att_list()
print("Choice 3")
mccoy.att_list()
print("Choice 4")
scott.att_list()

user1_input = input("Select TOS : 1, 2, 3, or 4: ")
print("You have selected:")
if user1_input == "1":
    tos_ch = kirk.name
    print(kirk.name)
    tos_tr += kirk.base

if user1_input == "2":
    tos_ch = spock.name
    print(spock.name)
    tos_tr += spock.base

if user1_input == "3":
    tos_ch = mccoy.name
    print(mccoy.name)
    tos_tr += mccoy.base

if user1_input == "4":
    tos_ch = scott.name
    print(scott.name)
    tos_tr += scott.base

print()
print("Choice 1")
picard.att_list()
print("Choice 2")
riker.att_list()
print("Choice 3")
crush.att_list()
print("Choice 4")
worf.att_list()

user2_input = input("Select TNG : 1, 2, 3, or 4: ")
print("You have selected:")
if user2_input == "1":
    tng_ch = picard.name
    print(picard.name)
    tng_tr += picard.base

if user2_input == "2":
    tng_ch = riker.name
    print(riker.name)
    tng_tr += riker.base

if user2_input == "3":
    tng_ch = riker.name
    print(crush.name)
    tng_tr += crush.base

if user2_input == "4":
    tng_ch = worf.name
    print(worf.name)
    tng_tr += worf.base

print()
print("Choice 1")
earth.plan_list()
print("Choice 2")
cestus.plan_list()
print("Choice 3")
ent.plan_list()
print("Choice 4")
deneb.plan_list()

user3_input = input("Select Battleground : 1, 2, 3, or 4: ")
print("You have selected:")
if user3_input == "1":
    pl_ch = earth.name
    print(earth.name)

if user3_input == "2":
    pl_ch = cestus.name
    print(cestus.name)
    tos_tr += cestus.base
    if user1_input == "1":
        tos_tr += 5

if user3_input == "3":
    pl_ch = ent.name
    print(ent.name)
    tng_tr += ent.base
    if user1_input == "1":
        tng_tr += 5

if user3_input == "4":
    pl_ch = deneb.name
    print(deneb.name)
    if side_boolean:
        tos_tr += deneb.base
    else:
        tng_tr += deneb.base

print()
print("Choice 1")
hand.mult_list()
print("Choice 2")
phase.mult_list()
print("Choice 3")
poly.mult_list()
print("Choice 4")
man.mult_list()

user4_input = input("Select Combat Modifications : 1, 2, 3, or 4 ")
print("You have selected:")
if user4_input == "1":
    mod_ch = hand.name
    print(hand.name)
    if user1_input == "2":
        tos_tr += 5

if user4_input == "2":
    mod_ch = phase.name
    print(phase.name)
    if user1_input != "2":
        tos_tr += 5

if user4_input == "3":
    mod_ch = poly.name
    print(poly.name)
    if user1_input != "3":
        tng_tr -= 10
        tos_tr -= 10

if user4_input == "4":
    print(man.name)
    tos_tr = input("Select TOS combat score ")
    tng_tr = input("Select TNG combat score ")

sel_list()

print("Fighting")
time.sleep(1)
print("Fighting")
time.sleep(1)
print("Fighting")
time.sleep(1)
print()

if tng_tr < tos_tr:
    print("The Original Series Wins!")

if tng_tr == tos_tr:
    print("Tie!")

if tng_tr > tos_tr:
    print("The Next Generation Wins!")
