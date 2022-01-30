from ast import Num


i = -1
neglaskin = 0
laskuri = -1
Lista = []
while(i != 0):
    i = input("Enter your value: ")
    Lista.append(i)
    print(i)

while(neglaskin < len(Lista)):
        if Lista[neglaskin] >= 0:
            laskuri += 1
        else:
            m = 7


print("laitoit näin monta kertaa negatiivisen arvon", laskuri)

#exercise 4.py
#Patrick Stenvik
#Ask for random values from the user and adds the to a list. When 0 is inserted 