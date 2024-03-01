# Factorial of a number using recursion

def fact(n):
    if n==1 or n==0:
        return 1
    
    else:
        res = n*fact(n-1) # function calling itself 5*4*3*2*1 -> 5*factorial(4) -> 4*factorial(3) -> 3*factorial(2) -> 2*factorial(1) -> 1*factorial(0)
        return(res)
    
n = 5
print(fact(n))

# OUTPUT:

# 120