"""Calcualte and print which standard the student is studying - Write a program to ask the user for his/her name 
and print 'Hello', user's name. 
Ask what year they were born.  
eg Hello Chitra, what year were you born?
get the year from the user. 
Calculate if the user is going to elementary school, middle school, highschool or college, based on users age. 
(hint - use if/elif)"""

name=input("Enter your name:")
print("Hello",name,",what year were you born?")
year_of_birth=int(input())
current_year=int(input("Enter the current year:"))
age=current_year-year_of_birth
if age>=5:
    if age>=5 and age<11:
        print("You are going to elementary school")
    elif age>=11 and age<14:
        print("You are going to middle school")
    elif age>=14 and age<18:
        print("You are going to highschool")
    else:
        print("You are going to college")
else:
    print("You are not eligible")

# OUTPUT:

# Enter your name:Sivakarthika
# Hello Sivakarthika ,what year were you born?
# 2003
# Enter the current year:2023
# You are going to college