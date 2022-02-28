# File:         Dice roller.py
# Created by:  Roope Iljanko & Patrick Stenvik
# Description:  Rolls 3 dice


import random as r


class DiceValue:
    def __init__(self):
        self.dvalue = 0

    def droll(self):
        self.roll = 0
        self.roll = self.roll + r.randint(0, 6)
        self.dvalue = self.roll
        

    def get_value(self):
        return self.dvalue
    
    def set_value(self,):
       return self.dvalue 



def main():
    x=0
    y=0
    val = input("Heitettyjen noppien määrä: ")

    my_dice = DiceValue()

    while(x!=val):
        print("you rolled a: ", my_dice.droll())
        p1 = my_dice.droll + p1
    while(y!=val):
        my_dice.droll()
        print("your opponent  rolled a: ", my_dice.droll())
    p2 = my_dice.droll + p2
    if(p1>p2):
        print("Voitit")
    elif(p1<p2):
        print("hävisit")
    else:
        print("tasapeli aloitetaan uudestaan")
        main()


main()