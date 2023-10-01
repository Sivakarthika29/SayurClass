''' Write a program for Collatz_conjecture.
Collatz_conjecture means - start with the input number.
For even number , divide by 2 (n/2)
For odd number 3n + 1
apply the above for the result number until the answer is 1. '''

num = int(input("Enter the number : "))
while num != 1:
    if num % 2 == 0:
        num = (num//2)
    else:
        num = 3*num+1
print(num)

# OUTPUT:
# Enter the number : 21
# 1
# Enter the number : 22
# 1

num = int(input("Enter the number : "))
count = 0
while num != 1:
    if num % 2 == 0:
        num = (num//2)
    else:
        num = 3*num+1
    count +=1
print(f"Number is reached 1 after these number of iteration : {count}")

# OUTPUT:
# Enter the number : 21
# Number is reached 1 after these number of iteration : 7
# Enter the number : 22
# Number is reached 1 after these number of iteration : 15

