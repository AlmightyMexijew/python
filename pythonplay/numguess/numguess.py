import random

ran_num = random.randint(0,10)
num_arr = []

guess = 0
while guess < 5:
    guess_input = input("Pick a number between 1 and 10. \n")
    if int(guess_input) == ran_num:
        print(f"You win! The number was {ran_num}")
        break
    else:
        print("Guess again you're wrong \n")
        guess = guess + 1
        num_arr.append(guess_input)
        print(f"Current guess count is {guess} \n")
        print(f"Current guesses are {num_arr} \n")
        continue

print("Game over")
