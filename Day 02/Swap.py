#Write a program that will swap two numbers.

first_num=int(input("Enter the first number:"))
sec_num=int(input("Enter the second number:"))
temp=first_num
first_num=sec_num
sec_num=temp
print("After Swapping, first number:", first_num,",second number:", sec_num)

# OUTPUT:

# Enter the first number:76     
# Enter the second number:23
# After Swapping, first number: 23 ,second number: 76