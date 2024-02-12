import random
word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign to variable chosen_word
chosen_word = random.choice(word_list)

#Ask user to guess a letter and assign it to guess, making all guesses lowercase
guess = input("Guess a letter: ").lower()

#Check if the letter guessed is one of the letters in the chosen_word
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

