''' Problem 1
Print the following pattern
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1

Observe how the nunmbers in the triangle are calculated. 
Do it in two steps. Work on the generating the numbers first in right angle triangle
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

And then work on the final output using proper indendation '''
        
# Pascal function 
def printPascal(n): 
    for line in range(1, n + 1):      # 1,2,3,4,5
        C = 1 
        for i in range(1, line + 1):   
            print(C, end = " ") 
            C = int(C * (line - i) / i)
        print("") 
 
n = 5 
printPascal(n)

''' OUTPUT:

1 
1 1 
1 2 1 
1 3 3 1
1 4 6 4 1 '''