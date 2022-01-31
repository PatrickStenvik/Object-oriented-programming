# File:         coin.py
# Source:       Tony Gaddis: Starting out with Python, fourth edition
# Modified by:  Sanna Maatta & Anne Jumppanen
# Description:  Coin object and tossing

import random

# Class definition

class Coin:
    def __init__(self):
        self.sideup = 'Heads'


    def toss_the_coin(self):
        toss = 0
        toss = random.randint(0,4)

        if toss == 0:
            self.sideup = 'Heads'
        elif toss == 1:
            self.sideup = 'Tails'
        elif toss == 2:
            self.sideup = 'coin drops on the ground and disappearson a rabbit hole'
        elif toss == 3:
            self.sideup = 'coin defies gravity and gets lost on a wormhole in space'
        else:
            self.sideup = 'Upright'

    def get_sideup(self):
        return self.sideup

# Main function definition

def main():

    my_coin = Coin()

    print("This side is up:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    print("Now this side is up:", my_coin.get_sideup())




# Calling the main function
main()
