import random
#get the names
names_string = input("Give me the names of those present, separated by a comma.  ")
names = names_string.split(",")

#randomly pick one
roulette = random.randint(0,len(names) - 1)

#declare who is paying
payer = names[roulette]
print(f'{payer} is going to buy the meal today!')
