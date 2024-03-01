"""1. Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

    All passwords must be at least 8 chars long. You can use RegEx if you want."""

import re
password = input("Enter your password : ")
lenOfPassword = len(password)
number_of_alpha = len(re.findall(r'[a-zA-Z]', password))
number_of_numeric = len(re.findall(r'[0-9]', password))
number_of_splchar = len(re.findall(r'[^a-zA-Z0-9]', password))
if (lenOfPassword >= 8):
    if (lenOfPassword == number_of_alpha) or (lenOfPassword == number_of_numeric) or (lenOfPassword == number_of_splchar):
        print("Your Password is Weak")
    elif (number_of_alpha >= 3) and (number_of_numeric >= 2) and (number_of_splchar >=1):
        if (lenOfPassword >= 16) :
            print("Your Password is Very Strong")
        else:
            print("Your Password is Strong")
    elif (number_of_alpha >= 1) and (number_of_numeric >= 1) and (number_of_splchar >=1):
        print("Your Password is Ok")
else:
    print("Please Enter atleast 8 chars")

# OUTPUT:

# Enter your password : Siva&87*
# Your Password is Strong