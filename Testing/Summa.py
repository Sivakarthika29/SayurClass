#http://www.milkaclarkestrokefoundation.org/uploads/2/4/5/9/2459046/bmi-index_orig.jpg

lines = int(input("Enter number of lines :")) 
number=1 
while(number<=lines):   # this loops run untill number reaches 10. After reaching 10 and executing the loop it will break the loop 
     if input("Enter space to print $ ") == " ": # asking user to click space bar to execute if statement 
        print(' '*(lines-number),end='')        # printing  (" " * number of lines - loop variable) 
        print(f"{'$ '*number}")     # printing "$ " * loop variable 
        number+=1   # increamenting loop variable 
     else: 
        break