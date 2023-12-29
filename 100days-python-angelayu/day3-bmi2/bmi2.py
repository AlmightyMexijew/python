#get height
height = float(input("What is your height in meters?"))
#get weight
weight = round(float(input("What is your weight in kg?")),2)
#tell them bmi then tell them if they're fat
bmicalc = round(weight / (height**2))
print(f'Your BMI is {bmicalc}.')
#analysis
if bmicalc < 18.5:
    print("You're underweight and need to eat a sandwich")
elif bmicalc > 35:
    print("You are clinically obese. Stop eating.")
elif bmicalc < 25 and bmicalc >= 18.5:
    print("You are normal weight. Congratulations!")
elif bmicalc > 30 and bmicalc < 35:
    print("You are obese")
else:
    print("You are slightly overweight")