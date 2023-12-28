#Welcome
print("Welcome to the tip calculator")
#Get bill
totalBill = float(input("What was the total bill? $"))
#Get percentage tip
tipPerc = int(input("Which percentage tip would you like to give? 10,12, or 15?"))
if tipPerc == 10:
    print("OK,10 percent it is")
elif tipPerc == 12:
    print("OK,12 percent it is")
else:
    print("OK,15 percent, very generous")
#How many people?
crowd = int(input("How many people to split the bill?"))
#final output
finalBill = (totalBill/crowd)
if tipPerc == 10:
    finalBill = finalBill + (finalBill * .10)
    finalBill = round(finalBill,2)
    print(f'Each person should pay ${finalBill}')
elif tipPerc == 12:
    finalBill = finalBill +(finalBill * .12)
    finalBill = round(finalBill,2)
    print(f'Each person should pay ${finalBill}')
else:
    finalBill = finalBill + (finalBill * .15)
    finalBill = round(finalBill,2)
    print(f'Each person should pay ${finalBill}')