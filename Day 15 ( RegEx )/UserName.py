'''2. Check if the username and password is correct. 
     Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
     passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
     name of the company mentioned in the username, followed by any 3 numbers.
     eg username : myname@sayur.com. password - mnamesay123 '''

import re
username = input("Enter the Username : ")
password = input("Enter the Password : ")
if '@' in username:
    if username.endswith(".com") or username.endswith(".edu") or username.endswith(".tech") or username.endswith("org"):
        if username[0] == password[0] and username[2] == password[1]:
            indexOfAT = username.index('@')
            beforeAT = username[indexOfAT - 3] + username[indexOfAT - 2] + username[indexOfAT - 1]
            afterAT = username[indexOfAT + 1] + username[indexOfAT + 2] + username[indexOfAT + 3]
            if  password[2:8] == (beforeAT + afterAT) and re.search(r'\d{3}$',password):
                print("Username and password is valid")
            else:
                print("Incorrect Password")
        else:
            print("Incorrect Password")
    else:
        print("Username should endswith '.com' or '.edu' or '.tech' or 'org' ")
else:
    print("Please enter valid username : @ is missing")
            


# OUTPUT:

# Enter the Username : myname@sayur.com
# Enter the Password : mnamesay123
# Username and password is valid
