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
