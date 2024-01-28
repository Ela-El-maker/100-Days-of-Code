print("Welcome to the rollercoaster!!!")

height = int(input("What is your height : "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age : "))
    if age < 12 :
        bill = 5
        print("You pay $5.")
    elif age <= 18:
        bill = 7
        print("You pay $7.")
    elif age >= 45 and age <= 55:
        print("HAve a free ride on us.")
    else:
        bill = 12
        print("You pay $12.")

    photo = input("Do you want a photo token : (Y/N)?")
    if photo == "Y":
        #adds $3 to the bill
        bill += 3
        
    print(f"Your bill is ${bill}.")

else :
    print("Sorry, you can't ride the rollercoaster")

