''' Problem 2:
Write a program to calculate avg marks of your class, in CS subject in the 
last 3 exams. '''

def cs_mark(no_of_students , total_mark_of_class):
    avg_mark = total_mark_of_class/no_of_students
    return avg_mark

no_of_students = int(input("Enter no of students : "))
for i in range(1,4):
    total_mark_of_class = int(input("Enter total mark of class in CS subject : "))
    result = cs_mark(no_of_students , total_mark_of_class)
    print(f"Avg marks of class in CS exam {i} : {int(result)}%")

# OUTPUT:

# Enter no of students : 60
# Enter total mark of class in CS subject : 4500
# Avg marks of class in CS exam 1 : 75%     
# Enter total mark of class in CS subject : 5523
# Avg marks of class in CS exam 2 : 92%     
# Enter total mark of class in CS subject : 5018
# Avg marks of class in CS exam 3 : 83%