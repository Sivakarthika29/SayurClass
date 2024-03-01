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

num = []
count = []
for i in range(2):
    n1 = int(input("Enter the number : "))
    num.append(n1)

for n in num:
    c=0
    while n != 1:
        if n % 2 == 0:
            n = (n//2)
        else:
            n = 3*n+1
        c +=1
    count.append(c)
minimum_count = min(count)
print(f"The number {num[count.index(minimum_count)]} has undergone minimum iterations {minimum_count}")

# OUTPUT:
# Enter the number : 21
# Enter the number : 22
# The number 21 has undergone minimum iterations 7