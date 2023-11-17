''' Problem 3:
In the input, find the first A and last A, print all the letters between these two A. 
If there is no A or 2nd A is not found, find the first B after the first A 
(if there is a A) and last B and print all the letters between these two B. 
If there is no B or 2nd B is not found, find the first C after the first B
(if there is a B) and last C and print all the letters between these two C. '''


def LetterBetweenAlpha(aString,alpha):
    aString.lower()
    alpha.lower()
    stringFound = False
    first_alpha = aString.find(alpha)
    if(first_alpha >= 0):
        last_alpha = aString.rfind(alpha)
        if(first_alpha != last_alpha):
            print(aString[first_alpha+1:last_alpha])
            stringFound = True
        else:
            print(f"No second {alpha} in the string")
    else:
        print(f"No {alpha}")
    return stringFound

string = input("Enter the string : ")
