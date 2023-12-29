#greet/take input
mynum = int(input("Hello, what is your number to check?"))
if mynum == 0:
    print("Error. Zero is not a number that cannot be checked.")
    quit()

if (mynum % 2) == 0:
    print("Your number is even")
else:
    print("Your number is odd")