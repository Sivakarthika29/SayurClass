"""Get a number from the user. Divide it by 3 and print the result. 
Divide again by 3 and print the result. Keep dividing until the number is less than 3. 
Print the number of times the number was divided."""

num=int(input("Enter the number:"))       #Get a number from the user
count=0                                   # Initialize the count variable
no_of_result=1                            # Initialize the number of result variable
divided_num=int(input("Enter the divided number:"))
while num>=3:                 #loop until the num is less than or equal 3
    num//=3
    print("Result",no_of_result,":",num)
    count+=1                #Increment the count value
    no_of_result+=1      #Increment the no of result value
print(count,"times the number was divided")

# OUTPUT:

# Enter the number:44
# Enter the divided number:3
# Result 1 : 14
# Result 2 : 4
# Result 3 : 1
# 3 times the number was divided