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
