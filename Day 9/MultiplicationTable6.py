'''Same as the above. Ask the user if they want only the basic or only the advanced or both.
Print what the user is asking. 
Also ask the user what number table they want to print'''



print("1.Only the basic\n2.Only the advance\n3.Basic & advance")
choice=int(input("Enter your choice: "))
table=int(input("Enter your table number: "))
print(f"Table {table}")
if choice == 1:
    for count in range(1,11):
        print(f"{table} * {count} = {table*count}")
elif choice == 2:
    for count in range(11,21):
        print(f"{table} * {count} = {table*count}")
elif choice == 3:
    print("Basic numbers")
    for count in range(1,11):
        print(f"{table} * {count} = {table*count}")
    print("Advanced numbers")
    for advanced_count in range(11,21):
        print(f"{table} * {advanced_count} = {table*advanced_count}")
else:
    print("Please enter your correct choice")