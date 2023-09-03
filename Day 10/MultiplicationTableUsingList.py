'''Challange questions
Ask the user which tables he/she wants to print (eg 2,9,7,12)
Also ask if they want to see the basic only or advanced only or both.
Hint - use list to get the user input and learn how to use a list in range statement'''

#Creating an empty list
tables = []
print("Enter -1 to finish \nEnter the table number: ")
while True:
    table_no =int(input())
    if table_no != -1:
        tables.append(table_no)
    else:
        break
print(tables)
print("1.Only the basic\n2.Only the advance\n3.Basic & advance")
choice=int(input("Enter your choice: "))
if choice ==1:
    start_value = 1
    end_value = 10
elif choice ==2:
    start_value = 11
    end_value = 20
elif choice == 3:
    start_value = 1
    end_value = 20  
else:
    print("Please enter your correct choice")
for i in tables:
    print(f"Table {i}")
    #iterating till the range
    for count in range(start_value , end_value + 1):
        print(f"{i} * {count} = {i * count}")
    print()

# OUTPUT:

# Enter -1 to finish      
# Enter the table number: 
# 2
# 9
# 7
# 12
# -1
# [2, 9, 7, 12]      
# 1.Only the basic   
# 2.Only the advance 
# 3.Basic & advance  
# Enter your choice: 1
# Table 2    
# 2 * 1 = 2  
# 2 * 2 = 4  
# 2 * 3 = 6  
# 2 * 4 = 8  
# 2 * 5 = 10 
# 2 * 6 = 12 
# 2 * 7 = 14 
# 2 * 8 = 16 
# 2 * 9 = 18 
# 2 * 10 = 20

# Table 9    
# 9 * 1 = 9  
# 9 * 2 = 18 
# 9 * 3 = 27 
# 9 * 4 = 36 
# 9 * 5 = 45 
# 9 * 6 = 54 
# 9 * 7 = 63 
# 9 * 8 = 72 
# 9 * 9 = 81
# 9 * 10 = 90

# Table 7
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# 7 * 4 = 28
# 7 * 5 = 35
# 7 * 6 = 42
# 7 * 7 = 49
# 7 * 8 = 56
# 7 * 9 = 63
# 7 * 10 = 70

# Table 12
# 12 * 1 = 12
# 12 * 2 = 24
# 12 * 3 = 36
# 12 * 4 = 48
# 12 * 5 = 60
# 12 * 6 = 72
# 12 * 7 = 84
# 12 * 8 = 96
# 12 * 9 = 108
# 12 * 10 = 120