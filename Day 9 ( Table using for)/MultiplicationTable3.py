'''Print the following. Learn how to use print with formatting
Learn how to print ********* using formatted print
My Tables
Table  1
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
**********
Table  2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
**********
Table  3
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
**********
End of tables'''

print("My Tables")
for table in range(1,4):
    print(f"Table {table}")
    for count in range(1,6):
        print(f"{table} * {count} = {table*count}")
    print("**********")
print("End of tables")


# OUTPUT:

# My Tables
# Table 1      
# 1 * 1 = 1    
# 1 * 2 = 2    
# 1 * 3 = 3    
# 1 * 4 = 4    
# 1 * 5 = 5    
# **********   
# Table 2      
# 2 * 1 = 2    
# 2 * 2 = 4    
# 2 * 3 = 6    
# 2 * 4 = 8    
# 2 * 5 = 10   
# **********   
# Table 3      
# 3 * 1 = 3    
# 3 * 2 = 6    
# 3 * 3 = 9    
# 3 * 4 = 12   
# 3 * 5 = 15   
# **********   
# End of tables
