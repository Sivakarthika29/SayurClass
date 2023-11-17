def LetterBetweenAlpha(aString,alpha):
    aString.lower()
    alpha.lower()
    first_alpha = aString.find(alpha)
    if(first_alpha >= 0):
        last_alpha = aString.rfind(alpha)
        if(first_alpha != last_alpha):
            print(aString[first_alpha+1:last_alpha])
        else:
            print(f"No second {alpha} in the string")
    else:
        print(f"No {alpha}")

string = input("Enter the string : ")
alphabet = input("Enter the character : ")
LetterBetweenAlpha(string,alphabet)



#https://github.com/SayurLearning/ProgrammingEssentials/blob/master/Programming%20Exercise/LogicalThinking/Functions2.py