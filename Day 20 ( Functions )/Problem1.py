''' Problem 1
In the input, find the first A and last A, print all the letters
 between these two A. '''

def printLettersBetnAandB(aString):
    firstA = aString.find("a")
    if(firstA >= 0):
        lastA = aString.rfind("a")
        if(lastA != firstA):
            print(aString[firstA+1:lastA])
        else:
            print("No second A")
    else:
        print("No A")

myString = input("Input a string : ") 
printLettersBetnAandB(myString)

# OUTPUT:

# Input a string : Siva is a woman
#  is a wom
