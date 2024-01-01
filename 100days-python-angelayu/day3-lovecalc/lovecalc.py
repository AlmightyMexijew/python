print("The Love Calculator is calculating your score...")
#take both names
name1 = input("What is your name?")
name2 = input("What is their name?")
#check number of times the letters in the word "TRUE" occurs(i.e. T,R,U,E)
name_total = name1 + name2
score = 0
letters = ['t','T','r','R','u','U','e','E']
for x in name_total:
    if x in letters:
        score += 1
#check number of times the letters in the word "LOVE" occurs(i.e. L,O,V,E)
score2 = 0
letters2 = ['l','L','o','O','v','V','e','E']
for y in name_total:
    if y in letters2:
        score2 += 1
#combine the numbers to make a 2 digit number
final_score = str(score) + str(score2)
final_score_int = int(final_score)
print(final_score_int)
#Scoring as follows:
# <10 or >90 should have the message "Your score is *x*, you go together like coke and mentos"
# range(40,50) should have the message "Your score is *y*, you are alright together."
# Otherwise, message will just be score. "Your score is *z*."
if final_score_int < 10 or final_score_int > 90:
    print(f'Your score is {final_score}. You go together like coke and mentos!')
elif 40 <=final_score_int <= 50:
    print(f'Your score is {final_score}, you are alright together.')
else:
    print(f"Your score is {final_score}")
