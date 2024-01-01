print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L?")
add_pepperoni = input("Do you want pepperoni? Y or N?")
extra_cheese = input("Do you want extra cheese? Y or N?")

small = 15
medium = 20
large = 25
pepperoni_small = 2
pepperoni_medium_large = 3
xcheese = 1
bill = 0

if size == "s" or size == "S":
    bill += small
elif size == "m" or size == "M":
    bill += medium
else:
    bill += large

if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "s" or size == "S":
        bill += pepperoni_small
    else:
        bill += pepperoni_medium_large


if xcheese == "y" or xcheese == "Y":
    bill += xcheese

print(f'Your final bill is: ${bill}')

    
