'''Suppose,  there are three students, first student brought Rs.1000 and second student brought 800 and another structure brough 1200. They went spent 2000 at weekend outing. They have 1000 amount is pending and we want to distribute back to the students. 
1.How do you want to distribute them ? 
write short progam to express your idea through python program
How to apply same logic, Suppose 10 students and each student brought 500.

through this homework, we are exploring  basic variables and operations and input and output operations.'''

student_1=int(input("Enter the Student_1 amount:"))
student_2=int(input("Enter the Student_2 amount:"))
student_3=int(input("Enter the Student_3 amount:"))
total=student_1+student_2+student_3
spent=int(input("Enter the total spent amount:"))
pending_amount=total-spent
print("Total amount:",total)
print("Final pending amount:",pending_amount)
print("Amount to pay back to student_1",pending_amount* (student_1/total))
print("Amount to pay back to student_2",pending_amount* (student_2/total))
print("Amount to pay back to student_3",pending_amount* (student_3/total))
