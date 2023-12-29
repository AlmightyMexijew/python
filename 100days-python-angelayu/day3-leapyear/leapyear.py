#get the year
myYear = int(input("What year would you like to check?"))

#check
if myYear % 4 == 0:
    if myYear % 100 == 0:
        if myYear % 400 == 0:
            print("It's a leap year")
        else:
            print("It's not a leap year")
    else:
        print("It's a leap year")
else:
    print("It's not a leap year")