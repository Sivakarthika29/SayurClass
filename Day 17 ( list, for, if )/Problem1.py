'''Problem 1
You have a list of student names and another list with their marks in CS. hard code the
values. no need to get it as input 
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed.'''


stud_name = ["Siva" , "Karthika" , "Ranjani" , "Shankar" , "Sekar"]
stud_mark = [34 , 56 , 78 , 23 , 98]
pass_stud = []
fail_count = 0

for i in range(len(stud_mark)):
    if stud_mark[i] >= 50:
        pass_stud.append(stud_name[i]+ ":" +str(stud_mark[i]))
    else:
        fail_count += 1
        
print("Pass Student : " + str(pass_stud))
print("Fail Count : " + str(fail_count))

# OUTPUT:

# Pass Student : ['Karthika:56', 'Ranjani:78', 'Sekar:98']
# Fail Count : 2