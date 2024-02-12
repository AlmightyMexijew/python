import random
word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign to variable chosen_word
chosen_word = random.choice(word_list)

#Ask user to guess a letter and assign it to guess, making all guesses lowercase
def make_a_guess():
    guess = input("Choose a letter  ")
    if len(guess) > 1:
        print("Error,try again")
        make_a_guess()
    else:
        print("Choice made")

make_a_guess()
#Check if the letter guessed is one of the letters in the chosen_word
if "guess" in chosen_word:
    print("Yes")
else:
    print("No")
