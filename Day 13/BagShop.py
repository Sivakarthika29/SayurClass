# ########## Problem 3 ############
# #Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
# #Customers can buy one or more bags at a time.
# #The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
# #Display total sales and total number of bags sold

# #initialize variables
# redBags, greenBags = 100, 200
# totalSales , totalBagsSold = 0

# while (totalSales < 10000 or totalBagsSold < 10) :
#     #Ask customer for input
#     #FillinMissingCode
    
#     #calculate total cost for the bags
#      #FillinMissingCode
#     totalSales +=  #FillinMissingCode
#     #increment no of bags sold
#     totalBagsSold +=  #FillinMissingCode
# print ( #FillinMissingCode)   


redBags, whiteBags = 100, 200
totalSales , totalBagsSold = 0 , 0
redBagAmount , whiteBagAmount = 1000, 1500

while (totalSales < 10000 or totalBagsSold < 10):
    noOfRedBags =int(input("How many Red bags you need? "))
    noOfWhiteBags =int(input("How many White bags you need? "))
     
    amount = (redBagAmount * noOfRedBags) + (whiteBagAmount * noOfWhiteBags)
    totalSales += amount 
    totalBagsSold += noOfWhiteBags + noOfRedBags 
    print("Your amount : " , amount) 

print ("Total sale amount: ",totalSales)  
print ("Total No of bags: ",totalBagsSold) 

# OUTPUT:

# How many Red bags you need? 3
# How many White bags you need? 4
# Your amount :  9000
# How many Red bags you need? 2
# How many White bags you need? 1
# Your amount :  3500      
# Total sale amount:  12500
# Total No of bags:  10 