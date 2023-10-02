#if input if 89, output should be 98 (swap the digits)

num=int(input("Enter the number:"))
swap_digit=0
while num>0:
    rem=num%10
    swap_digit=(swap_digit*10)+rem
    num=num//10
print("Swap the digits =",swap_digit)

# OUTPUT:

# Enter the number:987
# Swap the digits = 789