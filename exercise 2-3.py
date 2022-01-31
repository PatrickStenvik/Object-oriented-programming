

x = int(input("Anna tehtyjen tehtävien määrä: "))
if (x < 0):
    print("Error: exercise points cannot be < 0 or > 120.")
elif (x <= 60):
    print("arvosanasi on: 0")
elif (x <= 72):
    print("arvosanasi on: 1")
elif (x <= 84):
    print("arvosanasi on: 2")
elif (x <= 96):
    print("arvosanasi on: 3")
elif (x <= 108):
    print("arvosanasi on: 4")
elif (x <= 120):
    print("arvosanasi on: 5")
else:
    print("Error: exercise points cannot be < 0 or > 120.")
#exerscise 2-3.py
#Patrick Stenvik
#gives an average grade based on the points