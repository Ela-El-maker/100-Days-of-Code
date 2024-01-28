height = float(input("Height in m : "))
weight = float(input("Weight in kg : "))

bmi = round(weight/height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, and you are underweight {weight}")
elif bmi <25 :
    print(f"Your BMI is {bmi}, and you have normal weight {weight}")

elif bmi < 30 :
    print(f"Your BMI is {bmi}, and you are overweight {weight}")

elif bmi < 35 :
    print(f"Your BMI is {bmi}, and you are obese weight {weight}")

else:
    print(f"Your BMI is {bmi}, and you are clinical obese weight:  {weight}")