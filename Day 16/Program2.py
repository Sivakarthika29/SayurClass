''' 2. Input is an encrypted  string where there will be chars followed by number. The way to decrypt is 
to repeat the chars, by the number of times. Print the decrypted word and its length. 
If there are any special chars, all the chars between the number and special char are ignored.
 eg - ac2bd3 means acacbdbdbd. 
 ac2acc#cd3 acaccdcdcd '''

import re
encryptString = input("Enter the Encrypted string  : ") 

decryptedString= ""
tempWord =""
for letter in encryptString:
    if re.match(r'[0-9]',letter):  # checking if the letter is number
        decryptedString += tempWord * int(letter)
        tempWord = ""
    elif re.match(r'[a-zA-Z]',letter):  # checking if the letter is alpha
        tempWord = tempWord + letter
    else:                               # else - if the letter is any other spl char
        tempWord = ""

print(decryptedString)

# OUTPUT:

# Enter the Encrypted string  : ac2bd3
# acacbdbdbd