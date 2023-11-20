#buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user.
#find how many choc and cake the user can buy

# noOfCake = 0
# noOfChoc = 0
# #get budget
# #FillinMissingCode
# while (money >= 150) : 
#     if (money > 200) :
#         #buy choc
#         noOfChoc += 1
#         money -= 200
#     #FillinMissingCode for buying cake
# #print no of cakes and choc
# #FillinMissingCode

noOfCake = 0
noOfChoc = 0
money = int(input("Enter your budget : "))
while (money >= 150) : 
    if (money > 200) :
        noOfChoc += 1
        money -= 200
    else:
        noOfCake += 1
        money -= 150
print(f"No of cakes : {noOfCake} \nNo of chocolate : {noOfChoc}")

# OUTPUT:

# Enter your budget : 750
# No of cakes : 1    
# No of chocolate : 3
