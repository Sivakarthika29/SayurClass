''' Problem 2
You have a list of student names. you have one list each for their marks in CS, Math and English.
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement. '''

stud_name = ["Siva" , "Karthika" , "Ranjani" , "Shankar" , "Sekar"]
cs_mark = [98 , 64 , 96 , 98 , 23]
math_mark = [90 , 80 , 96 , 48 , 73]
eng_mark = [86 , 100 , 96 , 88 , 83]
new_stud_list = []

for i in range(len(stud_name)):
    if (cs_mark[i] >= 90 or math_mark[i] >= 90 or eng_mark[i] >= 90) and (cs_mark[i] >= 80 and math_mark[i] >= 80 and eng_mark[i] >= 80):
        new_stud_list.append(stud_name[i])
print(f"Names of Student scoring A and B grade{new_stud_list}")