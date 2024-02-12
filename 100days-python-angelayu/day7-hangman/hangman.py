import random
word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign to variable chosen_word
chosen_word = random.choice(word_list)
#Create empty list called display. Add _ to display
display = []
for x in range(len(chosen_word)):
    display.append("_")
print(display)
#Ask user to guess a letter and assign it to guess, making all guesses lowercase
def make_a_guess():
    guess = input("Guess a letter: ").lower()
    letter_check(guess)

#Check if the letter guessed is one of the letters in the chosen_word
def letter_check(guess):
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            print("Right")
            display[position] = (chosen_word[position])
        else:
            print("Wrong")
    print(display)
    make_a_guess()


make_a_guess()
