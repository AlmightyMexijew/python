#Input a Python list of student heights
student_heights = input().split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
##start
print(student_heights) #test to see what happens to input
num_students = len(student_heights)
print(num_students)
sumtotal = 0
for x in student_heights:
    sumtotal += x
    print(sumtotal)

def avgme():
    avg = sumtotal / num_students
    print(avg)
avgme()