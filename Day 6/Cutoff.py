"""We have 3 colleges - each college has a different cut off mark for engineering college admission.
Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
For eg, College 1 cut off - 93%, College 2 - 89% and college 3 - 97%. If the student's avg is, 94%, the student is eligible
 for admission in College 1 and College 2."""

college_1_cutoff = 93                                               
college_2_cutoff = 89
college_3_cutoff = 97
mark1=int(input("Enter your mark 1: "))
mark2=int(input("Enter your mark 2: "))
mark3=int(input("Enter your mark 3: "))
mark4=int(input("Enter your mark 4: "))
mark5=int(input("Enter your mark 5: "))
avg=(mark1+mark2+mark3+mark4+mark5)/5                          #calculate avg mark
print("Your cutoff mark ",avg )
if(avg >= college_3_cutoff):
    print("You are eligible for college 1, college 2 and college 3")
elif(avg >= college_1_cutoff):
    print("You are eligible for college 1 and college 2")
elif(avg >= college_2_cutoff):
    print("You are eligible for college 2")
else:
    print("You are not eligible")

# OUTPUT:

# Enter your mark 1: 98
# Enter your mark 2: 95
# Enter your mark 3: 93
# Enter your mark 4: 99
# Enter your mark 5: 89
# Your cutoff mark  94.8
# You are eligible for college 1 and college 2

