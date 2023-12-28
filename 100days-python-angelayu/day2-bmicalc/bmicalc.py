#enter height
height = float(input("What is your height in meters?"))
#enter weight
weight = float(input("What is your weight in kilograms?"))

#equation is BMI=Weight-in-kg/(height-in-meters)^2
bmi = weight/height**2
print(bmi)
bmi = round(bmi,2)
#output
print(bmi)