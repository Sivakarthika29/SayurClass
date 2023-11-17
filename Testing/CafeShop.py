import re


items = ["coffee","tea","vadai","biscuit"]
priceOfItems = [25, 15, 10, 20]
profitPerItem = [10, 5, 5, 5]
itemStocks = [150, 100, 250, 50]
quantityList = ["one","two","three","four","five","six","seven","eight","nine"]


cust_count = 0
cust_limit = 3
totalBill = 0
while cust_count < cust_limit:

    print("**** MENU CARD ****")
    for i in range(len(items)):
        print(f"{items[i]}\t- {priceOfItems[i]} Rs - Available Stock {itemStocks[i]}")
    
    cust_input = input("What do you want to buy? ")      
    cust_input = cust_input.lower()
    cust_input_list = cust_input.split()       
    cust_items = []
    quantity = []    
    for word in cust_input_list:
        if word in items:
            cust_items.append(word)
        elif re.match(r'[0-9]',word): 
            quantity.append(int(word)) 
        elif word in quantityList:
            quantity.append(quantityList.index(word) + 1) 
    if cust_items == []:
        print("Please check menu card")
        continue
  
    if quantity == []:
        word = input(f"How many {cust_items} you want ? ")
        if re.match(r'[0-9]',word): 
            quantity.append(int(word)) 
        elif word in quantityList:
            quantity.append(quantityList.index(word) + 1) 

    amount = 0
    for i in range(len(cust_items)):
        item_index = items.index(cust_items[i])
        itemStocks[item_index] -= quantity[i]
        amount += quantity[i] * priceOfItems[item_index]
        
    print("Your amount is =" ,amount)
    totalBill += amount
    cust_count += 1

print("TOTAL AMOUNT = " , totalBill)