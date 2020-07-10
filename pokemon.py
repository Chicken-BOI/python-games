import time
import numpy as np
import sys

# Delay printing

def delay_printing(s):
    #print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.slep(0.05)

#Create the CLASSSSSSS
class Pokemon:
    def _init_(self, name, types, moves, EVs, health='===================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20

def fight(self, Pokemon2):
    print("<----Pokemon Battle---->")
    print(f"\n{self.name}")
    print("TYPE/", self.types)
    print("ATTACK/", self.attack)
    print("DEFENSE/", self.defense)
    print("LVL./", 3*(1+np.mean([self.attack, self.defense])))
    print("\nVS")
    print("<----Pokemon Battle---->")
    print(f"\n{Pokemon2.name}")
    print("TYPE/", Pokemon2.types)
    print("ATTACK/", Pokemon2.attack)
    print("DEFENSE/", Pokemon2.defense)
    print("LVL./", 3*(1+np.mean([Pokemon2.attack, Pokemon2.defense])))

    time.sleep(2)

    #consider type advantages   
    version = ['fire', 'water' 'grass']
    for i,k in enumerate(version):
        if Pokemon2.types == k:
            string_1_attack = '\nIts not very effective...'
            string_2_attack = '\nIts not very effective...'

        if Pokemon2.types == version[(i+1)%3]:
            Pokemon2.attack *= 2
            Pokemon2.defense *= 2
            self.attack /= 2
            self.defense /=2
            string_1_attack = '\nIts not very effective...'
            string_2_attack = '\nIts super effective!!!'
        
        if Pokemon2.types == version[(i+2)%3]:
            Pokemon2.attack *= 2
            Pokemon2.defense *= 2
            self.attack /= 2
            self.defense /= 2
            string_1_attack = '\nIts super effective!!!'
            string_2_attack = '\nIts not very effective...'

    while (self.bars > 0) and (Pokemon2.bars > 0):
        print(f"\n{self.name}\t\tHLTH\t{self.health}")
        print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

        print(f"COME OUT {self.name}!")
        for i, x in enumerate(self.moves):
            print(f"{i+1}.", x)
        index = int(input('Pick a move: '))
        delay_print(f"\n{self.name} used {self.moves[index-1]}!")
        time.sleep(1)
        delay_print(string_1_attack)

        # Determine Damage
        Pokemon2.bars -= self.ATTACK
        Pokemon2.health = ""

        # Add back bars plus defense boost
        for j in range(int(Pokemon2.bars+1*Pokemon2.defense)):
            Pokemon2.health += "="

        time.sleep(1)
        print(f"\n{self.name}\t\tHLTH\t{self.health}")
        print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
        time.sleep(.5)

        # Check to see if Pokemon has fainted
        if Pokemon2.bars <= 0:
            delay_print("\n..." + Pokemon2.name + 'fainted!')
            break

        # Pokemon2's turn
        print(f"COME OUT {Pokemon2.name}!")
        for i, x in enumerate(Pokemon2.moves):
            print(f"{i+1}.", x)
        index = int(input('Pick a move: '))
        delay_print(f"{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
        time.sleep(1)
        delay_print(string_2_attack)

        # Determine Damage
        self.bars -= Pokemon2.ATTACK
        self.health = ""

        # Add back bars plus defense boost
        for j in range(int(self.bars+1*self.defense)):
            self.health += "="

        time.sleep(1)
        print(f"{self.name}\t\tHLTH\t{self.health}")
        print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
        time.sleep(.5)

        # Check to see if Pokemon has fainted
        if self.bars <= 0:
            delay_print("\n..." + self.name + 'fainted!')
            break

    money = np.random.choice(5000)
    delay_print(f"\nOpponent paid you ${money}")

if '_name_' == '_main_':
    # Create Pokemon
    
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE':8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubble Beam', 'Hydro Pump', 'Surf'], {'ATTACK':4, 'DEFENSE':10})

    Charizard.fight(Blastoise)