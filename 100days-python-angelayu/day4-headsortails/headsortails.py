import random
#Get input
userChoice = str(input("Heads or Tails?"))
if userChoice == "Heads" or userChoice == "heads":
    print("User picked Heads")
elif userChoice == "Tails" or userChoice == "tails":
    print("User picked Tails")
else:
    print("Error, input is only Heads or Tails")
    quit()
#toss the coin
tosser = random.randint(0,1)
#compare results
if tosser == 0:
    print('Tails')
    if userChoice == "tails" or userChoice == "Tails":
        print("You win")
    else:
        print("You lose")
else:
    print('Heads')
    if userChoice == "heads" or userChoice == "Heads":
        print("You win")
    else:
        print("You lose")