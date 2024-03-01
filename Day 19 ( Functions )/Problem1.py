''' No need to write actual code. Only pseudo code is enough
For eg 
#adds two numbers
def addnumber(num1, num2) #takes two numbers 
    #add the numbers and return the result
    return result 

#main code
#get input from users
result = addnumber(num1, num2)
print the result

Before writing code, make sure to read https://www.w3schools.com/python/python_functions.asp 

For all the following problems, identify what needs to be in a function, what will be its input
and its output parameters.

Problem 1:
Write a program to calculate your avg marks in CS subject in the last 3 exams. '''

def cs_mark(cs_mark1 , cs_mark2 , cs_mark3):
    avg_mark = (cs_mark1 + cs_mark2 + cs_mark3)/3
    return avg_mark

cs_mark1 = int(input("Enter CS mark 1 : "))
cs_mark2 = int(input("Enter CS mark 2 : "))
cs_mark3 = int(input("Enter CS mark 3 : "))
result = cs_mark(cs_mark1 , cs_mark2 , cs_mark3)
print(result)


# OUTPUT:

# Enter CS mark 1 : 68
# Enter CS mark 2 : 97
# Enter CS mark 3 : 85
# 83.33333333333333