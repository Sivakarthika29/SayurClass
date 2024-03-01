#Write code for drawing these patterns.
#Get width and length from the user.
# draw a empty rectangle woth char *
#eg 
'''
Row 5, col 7
* * * * * * *
*           *
*           *
*           *
* * * * * * *

'''

row = int(input("Enter no of rows : "))
col = int(input("Enter no of col : "))
print(f"Row {row}, Col {col}")
for i in range(row):
    for j in range(col):
        if (i == 0 or i == row-1) or (j == 0 or j == col-1):
            print("* ", end = "")
        else:
            print("  " , end ="")
    print()


''' OUTPUT
Enter no of rows : 5
Enter no of col : 7
Row 5, Col 7  
* * * * * * * 
*           * 
*           * 
*           * 
* * * * * * *    '''
