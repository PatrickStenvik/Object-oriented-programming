from pickle import APPEND


r = 1
Student = []
Grade = []
kokonais = 0
maara = 0 

while r == 1 :
    Name = input("Nimi: ")
    Student.append(Name)
    val = int(input("Arvosana: "))
    Grade.append(val)
    kysymys = int(input("kyllä = 0, Ei = 1: "))
    r = r + kysymys

for ele in range(0, len(Grade)):
    kokonais = kokonais + Grade[ele]

for ele in range(0, len(Student)):
    maara = maara + 1

keski = kokonais / maara

if (keski < 0):
    print("Error: exercise points cannot be < 0 or > 120.")
elif (keski <= 60):
    print("Keskiarvo on: 0")
elif (keski <= 72):
    print("Keskiarvoon: 1")
elif (keski <= 84):
    print("Keskiarvo on: 2")
elif (keski <= 96):
    print("Keskiarvo on: 3")
elif (keski <= 108):
    print("Keskiarvo on: 4")
elif (keski <= 120):
    print("Keskiarvo on: 5")
else:
    print("Error: exercise points cannot be < 0 or > 120.")
#exerscise 2-5.py
#Patrick Stenvik
#gives an average grade based on the points given per student 