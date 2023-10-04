''' Problem 2:
Write a program to calculate avg marks of your class, in CS subject in the 
last 3 exams. '''

def cs_mark(no_of_students , total_mark_of_class):
    avg_mark = total_mark_of_class/no_of_students
    return avg_mark

no_of_exam = 3
#total_avg = 0
no_of_students = int(input("Enter no of students : "))
for i in range(no_of_exam):
    total_mark_of_class = int(input("Enter total mark of class in CS subject : "))
    result = cs_mark(no_of_students , total_mark_of_class)
    #total_avg += result
    print(f"Avg marks of class in CS exam {i} : {int(result)}%")
#total_avg_of_last_3_exam = total_avg / no_of_exam
#print(f"Total avg of last 3 exams : {total_avg_of_last_3_exam}")

# OUTPUT:

# Enter no of students : 60
# Enter total mark of class in CS subject : 4500
# Avg marks of class in CS exam 1 : 75%     
# Enter total mark of class in CS subject : 5523
# Avg marks of class in CS exam 2 : 92%     
# Enter total mark of class in CS subject : 5018
# Avg marks of class in CS exam 3 : 83%