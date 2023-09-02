"""Calcualte and print users age - Write a program to ask the user for his/her name and print 'Hello', user's name.
Ask what year they were born.  get the year from the user. Print 'You are <age> years old'."""

current_year=int(input("Enter the current year:"))
name=input("Enter your name:")
year_of_birth=int(input("What is your year of birth?"))
age=current_year-year_of_birth
print("Hello "+name)
print("You are",age,"years old")

# OUTPUT:

# Enter the current year:2023
# Enter your name:Sivakarthika
# What is your year of birth?2003
# Hello Sivakarthika  
# You are 20 years old