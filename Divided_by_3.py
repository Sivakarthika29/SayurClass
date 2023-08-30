"""Get a number from the user. Divide it by 3 and print the result. 
Divide again by 3 and print the result. Keep dividing until the number is less than 3. 
Print the number of times the number was divided."""

num=int(input("Enter the number:"))
count=0
no_of_result=1
divided_num=int(input("Enter the divided number:"))
while num>=3:        #loop until the num is less than 
    num//=3
    print("Result",no_of_result,":",num)
    count+=1
    no_of_result+=1
print(count,"times the number was divided")

