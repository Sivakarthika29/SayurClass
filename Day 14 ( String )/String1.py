# ########## Program 1
# #Get an input string from the user. Add a space at every 3rd char.
# #eg input = abcdefg , output = ab cd ef g
# inputString = #FillinMissingCode
# i = 0 #counter to track the chars
# newString = ""
# while i < len(inputString):
#     newString += #FillinMissingCode (assign the from i, i+1 of inputString)
#     newString += " " #add space
#     i+=2
# #check to add the chars at the end
# #FillinMissingCode

# print (newString)

inputString = input("Enter the String : ")
i = 0 #counter to track the chars
newString = ""
while i < len(inputString):
    if (i+1) < len(inputString):
        newString += inputString[i] + inputString[i + 1]
    else:
        newString += inputString[i]
    newString += " " #add space
    i+=2

print (newString)

# OUTPUT:

# Enter the String : abcdefg
# ab cd ef g 