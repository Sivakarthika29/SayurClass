''' Problem 3:
Write a program to calculate avg marks for each student and no of students whose 
avg is above 75% in CS subject in the last 3 exams. '''

noOfStudents = int(input("Enter no of students : "))
avg_is_above_75 = 0
def cs_mark(cs_mark1 , cs_mark2 , cs_mark3):
    avg_mark = (cs_mark1 + cs_mark2 + cs_mark3)/3
    return avg_mark

for i in range(1,noOfStudents+1):
    cs_mark1 = int(input("Enter CS mark 1 : "))
    cs_mark2 = int(input("Enter CS mark 2 : "))
    cs_mark3 = int(input("Enter CS mark 3 : "))
    result = cs_mark(cs_mark1 , cs_mark2 , cs_mark3)
    print(f"Avg mark : {int(result)}")
    if result > 75:
        avg_is_above_75 += 1
print(f"No of students avg mark above 75% : {avg_is_above_75}")

# OUTPUT:

# Enter no of students : 3
# Enter CS mark 1 : 56
# Enter CS mark 2 : 34
# Enter CS mark 3 : 45
# Avg mark : 45     
# Enter CS mark 1 : 98
# Enter CS mark 2 : 99
# Enter CS mark 3 : 98
# Avg mark : 98     
# Enter CS mark 1 : 97
# Enter CS mark 2 : 96
# Enter CS mark 3 : 87
# Avg mark : 93
# No of students avg mark above 75% : 2