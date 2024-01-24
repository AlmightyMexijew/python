#Password Generator Project
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total_nr = nr_letters + nr_symbols + nr_numbers
#easy: generate in sequence (letters,sym,num)  == fghf$&23
easy_let_list = []
easy_sym_list = []
easy_num_list = []
final_easy_list = []
for x in range(0,nr_letters):
    easy_let_list.append(random.choice(letters))
for x in range(0,nr_symbols):
    easy_sym_list.append(random.choice(symbols))
for x in range(0,nr_numbers):
    easy_num_list.append(random.choice(numbers))
final_easy_list = easy_let_list + easy_sym_list + easy_num_list
final_easy_list = ''.join(final_easy_list)
print(final_easy_list)
#hard: generate at random 
hard_list = []

for x in range(total_nr+1):
    choice = random.choice(["letters","symbols","numbers"])
    if choice == 'letters':
        if nr_letters > 0:
            hard_list.append(random.choice(letters))
            nr_letters -= 1
    elif choice == 'symbols':
        if nr_symbols > 0:
            hard_list.append(random.choice(symbols))
            nr_symbols -= 1
    elif choice == 'numbers':
        if nr_numbers > 0:
            hard_list.append(random.choice(numbers))
            nr_numbers -= 1

hard_password = ''.join(hard_list)
print(f"Hard Password: {hard_password}")