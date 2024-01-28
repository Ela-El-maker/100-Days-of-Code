print("Welcome to the Pizzling Pizza")

size = input("What size of pizza do you want: (S,M,L) ? ")
addPepporoni = input("Do you want to add pepporoni : (Y/N) ? ")
extraCheese = input("Do you want to add extra cheese : (Y/N) ? ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if addPepporoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extraCheese == "Y":
    bill += 1

print(f" Your bill is ${bill}")