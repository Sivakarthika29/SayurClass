########## Program 2
#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM
        
# myName = #FillinMissingCode
# for letter in myName:
#     print(#FillinMissingCode)
        
        
myName = input("Enter the name : ")
ans = ""
for letter in myName:
    ans += letter
for x in range(len(myName)):
    for y in range(x + 1):
        print(ans[y], end=" ")
    print()

# OUTPUT:

# Enter the name : RAM
# R     
# R A   
# R A M 