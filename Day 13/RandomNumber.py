
######## Problem 2 ###############
# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number

# import #FillinMissingCode
# computerNo = random.randint(3, 9)

# attempt = 0
# while(True):
#     userNo = int (#FillinMissingCode)
#     #FillinMissingCode
#     attempt +=1

# print ("User guessed the number in ", attempt, "attempts")

import random
computerNo = random.randint(3, 9)

attempt = 0
while(True):
    userNo = int (input("Enter the number: "))
    if computerNo == userNo:
        print("User guess the number correctly")
        break
    elif computerNo < userNo:
        print("High")
    else:
        print("Low")
    attempt +=1
print ("User guessed the number in ", attempt, "attempts")    


# OUTPUT:

# Enter the number: 4
# Low
# Enter the number: 5
# Low
# Enter the number: 6
# Low
# Enter the number: 7
# User guess the number correctly       
# User guessed the number in  3 attempts