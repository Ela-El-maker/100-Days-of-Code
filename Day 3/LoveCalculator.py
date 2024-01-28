print("Welcome to the Love Calculator")
name1 = input("Your name : ");
name2 = input("Their name : ");

combinedString = name1 + name2
lowerCaseString = combinedString.lower()

t = lowerCaseString.count('t')
r = lowerCaseString.count('r')
u = lowerCaseString.count('u')
e = lowerCaseString.count('e')

true = t + r + u + e

l = lowerCaseString.count('l')
o = lowerCaseString.count('o')
v = lowerCaseString.count('v')
e = lowerCaseString.count('e')

love = l + o + v + e
loveScore = int(str(true) + str(love))

if loveScore < 10 or loveScore > 90:
    print(f"{name1} loves {name2} and their score is {loveScore}")
    print("You got together like coke and mentos")
elif loveScore >= 40 and loveScore <= 50:
    print(f"{name1} consumes {name2} and their score is {loveScore} you are alright together.")
else:
    print(f"Your love score is {loveScore} ") 

print(f"{name1} loves {name2} and their score is {loveScore}")
