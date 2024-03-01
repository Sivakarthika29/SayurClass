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
Karthika_marks = [98, 90, 86]
Ranjani_marks = [64, 80, 100]
Shankar_marks = [96, 96, 96]
Siva_marks = [98, 48, 88]
Sathish_marks = [23, 73, 83]
all_marks = [ Karthika_marks , Ranjani_marks , Shankar_marks , Siva_marks , Sathish_marks ]
best_stud_list = []
j=0

for i in range(len(stud_name)):
    marks = all_marks[i]
    if (marks[j] >= 90 or marks[j+1] >= 90 or marks[j+2] >= 90) and (marks[j] >= 80 and marks[j+1] >= 80 and marks[j+2] >= 80):
        best_stud_list.append(stud_name[i])
print(f"Names of Student scoring A and B grade {best_stud_list}")


''' OUTPUT:

Names of Student scoring A and B grade ['Karthika', 'Shankar']
'''