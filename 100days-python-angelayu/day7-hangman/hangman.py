import random
word_list = ["aardvark", "baboon", "camel"]
lives = 5
#Randomly choose a word from the word_list and assign to variable chosen_word
chosen_word = random.choice(word_list)

#Ask user to guess a letter and assign it to guess, making all guesses lowercase
def make_a_guess():
    guess = str(input("Choose a letter:  "))
    guess = guess.lower()
    if len(guess) > 1:
        print("Your guess is too big. Pick again")
        make_a_guess()
    else:
        print(guess)
        
#Check if the letter guessed is one of the letters in the chosen_word
def in_word():
    if guess in chosen_word:
        print("It's there")
    else:
        print("Not there")
        lives -= 1
        print(lives)

make_a_guess()
