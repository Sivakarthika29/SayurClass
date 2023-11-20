''' Problem #2
you have a list of student names and another list with their marks in CS. 
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed. '''

name = ["Karthika","Ranjani","Shankar","Siva","Sathish"]  
cs_marks = [68,45,97,50,32]
pass_marks = 50
pass_marks_students = []
no_of_fail_students = 0
for i in range(len(name)):                  # len(name) = 5 (i = 0, 1, 2, 3, 4)
    if (cs_marks[i] >= pass_marks):             
        pass_marks_students.append(name[i] + ":" + str(cs_marks[i]) )
    else:
        no_of_fail_students += 1
print("Students with pass marks : " , pass_marks_students)
print("No of Fail students : ", no_of_fail_students)


''' 
OUTPUT

Students with pass marks :  ['Karthika:68', 'Shankar:97', 'Siva:50']
No of Fail students :  2 
'''