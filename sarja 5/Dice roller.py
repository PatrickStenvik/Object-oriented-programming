# File:         Dice roller.py
# Created by:  Roope Iljanko & Patrick Stenvik
# Description:  Rolls 3 dice


import random as r


class DiceValue:
    def __init__(self):
        self.dvalue = 0

    def droll(self):
        self.roll = r.randint(0, 6)
        
        self.roll = self.roll + r.randint(0, 6)
        
        self.roll = self.roll + r.randint(0, 6)
        self.dvalue = self.roll
        

    def get_value(self):
        return self.dvalue
    
    def set_value(self,):
       return self.dvalue 



def main():

    my_dice = DiceValue()

    print("you rolled a: ", my_dice.droll())
    p1 = my_dice.droll
    my_dice.droll()

    print("your opponent  rolled a: ", my_dice.droll())
    p2 = my_dice.droll
    if(p1>p2):
        print("Voitit")
    else:
        print("hävisit")


main()