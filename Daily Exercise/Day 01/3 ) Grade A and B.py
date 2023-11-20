''' Problem #3
you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement. '''

stud_name = ["Karthika","Ranjani","Shankar","Siva","Sathish"]
marks = [98 , 64 , 96 , 98 , 23 , 90 , 80 , 96 , 48 , 73 , 86 , 100 , 96 , 88 , 83]
best_stud_list = []

for i in range(len(stud_name)):
    if (marks[i] >= 90 or marks[i+5] >= 90 or marks[i+10] >= 90) and (marks[i] >= 80 and marks[i+5] >= 80 and marks[i+10] >= 80):
        best_stud_list.append(stud_name[i])
print(f"Names of Student scoring A and B grade {best_stud_list}")


''' OUTPUT:

Names of Student scoring A and B grade ['Karthika', 'Shankar']
'''