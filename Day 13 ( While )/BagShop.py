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
    saleRedBagAmount , saleWhiteBagAmount = 0, 0
    print("Available Red Bags : ", redBags)
    if redBags >0 and redBags <= 100:
        noOfRedBags =int(input("How many Red bags you need? "))
        redBags -= noOfRedBags
        saleRedBagAmount = redBagAmount * noOfRedBags
    else:
        print("Red Bags is not Available")
    
    print("Available White Bags : ", whiteBags)
    if  whiteBags >0 and whiteBags <= 200:
        noOfWhiteBags =int(input("How many White bags you need? "))
        whiteBags -=  noOfWhiteBags
        saleWhiteBagAmount = whiteBagAmount * noOfWhiteBags
        totalAmount = saleRedBagAmount + saleWhiteBagAmount
        totalSales += totalAmount 
        totalBagsSold += noOfWhiteBags + noOfRedBags 
        print("Your amount : " , totalAmount) 
    else:
        print("White Bags is not Available")

print ("Total sale amount: ",totalSales)  
print ("Total No of bags: ",totalBagsSold) 

# OUTPUT:

# Available Red Bags :  100
# How many Red bags you need? 5
# Available White Bags :  200   
# How many White bags you need? 2
# Your amount :  8000
# Available Red Bags :  95    
# How many Red bags you need? 1
# Available White Bags :  198   
# How many White bags you need? 2
# Your amount :  4000      
# Total sale amount:  12000
# Total No of bags:  10