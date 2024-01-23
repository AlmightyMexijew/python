#Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

#calculate highest score
highest_score = 0
for x in range(0,len(student_scores)):
    if(student_scores[x] > highest_score):
        highest_score = student_scores[x]
        
print(f'The highest score is {highest_score}')
#calculate lowest score
lowest_score = student_scores[0]
for x in range(0,len(student_scores)):
    if(student_scores[x] < lowest_score):
        lowest_score = student_scores[x]
print(f'lowest_score is {lowest_score}')
#calculate avg score
num_students = len(student_scores)
sum_students = 0
for x in range(0,len(student_scores)):
    sum_students += student_scores[x]
avg_students = sum_students / num_students
print(f'The number of students is{num_students}')
print(f'The sum total of scores is {sum_students}')
print(f'The avg score is {avg_students}')
