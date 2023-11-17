# import random

# randomNUm = random.randint(1,4)
# print(randomNUm)

import re
password = input("Enter passwords : ")
# number_of_alpha =(re.findall(r'[a-zA-Z]$', password))
# print(number_of_alpha)

if re.match("^[a-zA-Z]+$",password):
        print("Weak password-only alphabets")