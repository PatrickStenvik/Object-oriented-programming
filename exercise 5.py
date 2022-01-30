from ast import Num


i = -1
neglaskin = 0
laskuri = -1
Lista = []
parilliset = 0

while i != 0:
    i = input("Enter your value: ")
    Lista.append(i)
    print(i)

while(neglaskin < len(Lista)):
        if Lista[neglaskin] >= 0:
            laskuri += 1
        else:
            m = 7

while(neglaskin < len(Lista)):
    if Lista[neglaskin] %2 == 0:
        parilliset += 1
    else:
        m = 8



print("laitoit näin monta kertaa negatiivisen arvon", laskuri)
print("parillisten lukujen määrä", parilliset)
#exercise 5.py
#Patrick Stenvik
#Ask for random values from the user and adds them to a list. When 0 is inserted its supposed to stop asking and count the values under 0
#Does not work atm. No clue why. It just keeps asking numbers after the 0 is given.