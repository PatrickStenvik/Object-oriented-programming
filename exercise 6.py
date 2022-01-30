from ast import Num


i = -1
neglaskin = 0
parlaskin = 0
laskuri = -1
Lista = []
parilliset = 0
trilaskin = 0
kolmi = 0

while i != 0:
    i = input("Enter your value: ")
    Lista.append(i)
    print(i)

while(neglaskin < len(Lista)):
        if Lista[neglaskin] >= 0:
            laskuri += 1
            neglaskin += 1
        else:
            neglaskin += 1

while(parlaskin < len(Lista)):
    if Lista[parlaskin] %2 == 0:
        parilliset += 1
        parlaskin += 1
    else:
        parlaskin += 1

while(trilaskin < len(Lista)):
    if Lista[trilaskin] %3 == 0:
        kolmi += 1
        trilaskin += 1
    else:
        trilaskin += 1

print("laitoit näin monta kertaa negatiivisen arvon", laskuri)
print("parillisten lukujen määrä", parilliset)
print("kolmella jaollisten lukujen määrä", kolmi)
#exercise 6.py
#Patrick Stenvik
#Ask for random values from the user and adds them to a list. When 0 is inserted its supposed to stop asking and count the values under 0
#Does not work atm. No clue why. It just keeps asking numbers after the 0 is given.