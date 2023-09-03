#Calculate the Grade for a student, using 3 marks.
# The student has 100 marks in any one subject, Grade is A.
# if the student has 90 or above in any one subject  Grade is B
# if the student has 60 or above in any one subject  Grade is C
# if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.


mark1=int(input("Enter your marK 1: "))
mark2=int(input("Enter your marK 2: "))
mark3=int(input("Enter your marK 3: "))
if mark1 ==100 or mark2 == 100 or mark3 == 100:
    print("Your Grade is A")
elif mark1 >= 90 or mark2 >= 90 or mark3 >= 90:
    print("Your Grade is B")
elif mark1 >= 60 or mark2 >= 60 or mark3 >= 60:
    print("Your Grade is C")
elif mark1 <= 50 and mark2 <= 50 and mark3 <= 50:
    print("Your Grade is F")
else:
    print("Your Grade is D")

# OUTPUT:

# Enter your marK 1: 96
# Enter your marK 2: 95
# Enter your marK 3: 99
# Your Grade is B