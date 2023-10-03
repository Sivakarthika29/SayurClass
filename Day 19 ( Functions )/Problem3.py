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
    if result > 75:
        avg_is_above_75 += 1
print(f"No of students avg mark above 75% : {avg_is_above_75}")