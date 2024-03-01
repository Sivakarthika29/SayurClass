''' problem #5
In your college Python is taught in 3 different departments by the same professor. 
For each dept, get the no of students studying Python and their marks in the final exam 
Get the input as comma seperated string

Find the top 3 marks in each class
Find the top 3 marks in all classes are combined.
Find the avg mark of students with passing mark in each class and the classes combined.
Find which class has the best average mark and least number of failed students. '''

no_of_dept = 3
# student_data ={
# "cse"   : [45,32,56,78,90],
# "csd"   : [56,89,34,21,89],
# "aids"  : [34,60,78,56,90],
# }   
student_data = {}

for i in range(no_of_dept):
    dept_name = input(f"Enter the dept{i+1} name : ")
    no_of_students = int(input(f"Enter no of students in {dept_name} : "))
    marks_list = input(f"Enter {no_of_students} marks : ").split(",")

    student_data[dept_name] = marks_list  # updating student data , dept is key , mark in value

list_of_dept = list(student_data.keys())   # ["cse","csd","aids"]
all_dept_marks = [] 
# top 3 marks in each class
for dept in list_of_dept:
    marks = student_data[dept]
    marks.sort(reverse=True)
    print(f"Top 3 marks in {dept} - {marks[:3]}")

    all_dept_marks.extend(student_data[dept])  # [45,32,56,78,90, 56,89,34,21,89, 34,60,78,56,90]

# top 3 marks in all classes are combined.
all_dept_marks.sort(reverse=True)
print("\nTop 3 marks in all dept : ",all_dept_marks[:3])
print()

failed_students_count =[]  
avg_each_dept = []          # [34,56,78]
# avg marks for each class
for dept in list_of_dept:
    sum = 0
    failed_count = 0
    marks = student_data[dept]
    for mark in marks:
        if int(mark) >= 50:
            sum += int(mark)
        else:
            failed_count += 1
    avg = sum / len(marks)
    failed_students_count.append(failed_count)  # for finding least avg
    print(f"The avg mark of {dept} dept : {avg}")
    avg_each_dept.append(avg)   # for finding best avg
     

# avg marks for all dept
sum = 0
for mark in all_dept_marks:
    if int(mark) >= 50:
        sum += int(mark)
avg_all_dept = sum / len(all_dept_marks)
print(f"\nAvg marks of all dept : {avg_all_dept}")

best_avg_dept = list_of_dept[avg_each_dept.index(max(avg_each_dept))]
print(f"\nBest avg dept : ",best_avg_dept)

least_failed_dept = list_of_dept[failed_students_count.index(min(failed_students_count))]
print("\nleast Failed students dept : " , least_failed_dept)



'''
OUTPUT:

Enter the dept1 name : cse
Enter no of students in cse : 5
Enter 5 marks : 45,32,56,78,90
Enter the dept2 name : csd
Enter no of students in csd : 5
Enter 5 marks : 56,89,34,21,89
Enter the dept3 name : aids
Enter no of students in aids : 5
Enter 5 marks : 34,60,78,56,90
Top 3 marks in cse - ['90', '78', '56']
Top 3 marks in csd - ['89', '89', '56']
Top 3 marks in aids - ['90', '78', '60']

Top 3 marks in all dept :  ['90', '90', '89']

The avg mark of cse dept : 44.8
The avg mark of csd dept : 46.8
The avg mark of aids dept : 56.8

Avg marks of all dept : 49.46666666666667

Best avg dept :  aids

least Failed students dept :  aids '''