######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines


line = int(input("Enter the number of lines: "))
print("Enter space to print $")
for i in range(line):
    if input() == " ":
        print(" " * (line-i) + "$ " * (i+1))
    else:
        break
for j in range(line - 1):
    if input() == " ":
        print(" " * (j+2) + "$ " * (line -1-j) )
    else:
        break

# OUTPUT:

# Enter the number of lines: 5
# Enter space to print $
 
#      $ 
 
#     $ $ 
 
#    $ $ $ 
 
#   $ $ $ $ 
 
#  $ $ $ $ $ 
 
#   $ $ $ $ 
 
#    $ $ $ 
 
#     $ $ 
 
#      $ 
