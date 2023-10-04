''' Problem 5:
Write a program to sort an array of numbers in ascending order. Use functions. '''

def my_function(list):
    sorted_list = sorted(list)
    return sorted_list
list = [56 , 43 , 12 , 78]
result = my_function(list)
print(f"Sorted list : {result}")

# OUTPUT:

# Sorted list : [12, 43, 56, 78]


