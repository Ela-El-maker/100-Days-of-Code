choice1 = input("You are at a crossroad, where do you want to go? \"left\" or \"right\" : ").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake. Type 'wait' to wait for a boat. Type 'Swim' to swim across.").lower()

    if choice2 == "wait":
        choice3 = input("Which color do you choose. Red, Yellow, Blue : ").lower()

        if choice3 == "red":
            print("A room full of fire. Game over!!!")
        elif choice3 == "yellow":
            print("You found the treasure. You win!")
        elif choice3 == "blue":
            print("A room full of beasts. Game over!!!")
        else:
            print("That door doesnt Exist. Game over!!!")
        
    else:
        print("You got attacked by an angry trout. Game over!!!")
else:
    print("You fell into a hole. Game over!!!")