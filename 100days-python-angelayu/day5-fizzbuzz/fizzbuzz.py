#Rules:
#Print each number from 1 to 100 in turn, including 100
for x in range(1,101,1):
    if(x % 3 == 0):
        if(x % 5 == 0):
            print("fizzbuzz")
        else:
            print("fizz")
    elif(x % 5 == 0):
        print("buzz")
    else:
        print(x)