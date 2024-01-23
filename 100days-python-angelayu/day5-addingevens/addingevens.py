target = int(input()) #Enter a number between 0 and 1000

#check if it's in the bounds 0 - 1000
if(target > 1000):
    print("Target is too big. Pick something smaller than 1000")
    quit()
elif(target < 0):
    print("Target is too small and must be at least 0")
    quit()

even_list = []
even_total = 0
for x in range(0,target):
    if (x % 2 == 0):
        even_list.append(x)
        even_total += x
if (target % 2 == 0):
        even_list.append(target)
        even_total += target

print(even_list)
print(f'The final total of all evens is {even_total}')
