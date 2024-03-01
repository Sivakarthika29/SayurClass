"""Ask the user to input 3 numbers. Ask the user if they want to find the max of these numbers or minimum.
Find the answer and print."""

num_1=int(input("Enter the 1st number:"))
num_2=int(input("Enter the 2nd number:"))
num_3=int(input("Enter the 3rd number:"))
print("Do you want to find the maximum or minimum of these numbers?")
print("1.Find the maximum number\n2.Find the minimum number\n3.Exit")
choice=int(input("Enter your choice:"))
if choice==1:
    if num_1>num_2 and num_1>num_3:
        print(num_1,"is maximum number")
    elif num_2>num_1 and num_2>num_3:
        print(num_2,"is maximum number")
    else:
        print(num_3,"is maximum number")
elif choice==2:
    if num_1<num_2 and num_1<num_3:
        print(num_1,"is minimum number")
    elif num_2<num_1 and num_2<num_3:
        print(num_2,"is minimum number")
    else:
        print(num_3,"is minimum number")
else:
    print("You are Exit\nTHANK YOU!!!!")

# OUTPUT:

# Enter the 1st number:45
# Enter the 2nd number:76
# Enter the 3rd number:12
# Do you want to find the maximum or minimum of these numbers?
# 1.Find the maximum number
# 2.Find the minimum number
# 3.Exit
# Enter your choice:1
# 76 is maximum number