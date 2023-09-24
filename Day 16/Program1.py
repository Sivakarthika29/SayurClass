''' String manipulation exercises. Use builtin functions as needed.

1. Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
When the customer comes in, vendor asks "What do you want to buy?" .
The customer can say "I want apple", or "Apple" or "three apple" or something like that.
Your program will find out what fruit the customer is asking. 
Your program will also find, if the customer already asked for the quantity of the fruit
(one apple or 5 orange etc).
Print the quantity if the customer says the quantity. If not, ask him how much he wants.
Hint : Use string manipulation and lists. https://www.w3schools.com/python/python_ref_string.asp 
You can limit the quantity to single digit number. '''

import re
fruitsList = ["apple" , "orange", "banana"]
quantityList = ["one","two","three","four","five","six","seven","eight","nine"]
cust_input = input("What do you want to buy? ")      # I want apple
cust_input = cust_input.lower()
cust_input_list = cust_input.split()        # split in cust_input eg:['i', 'want', 'apple']

fruit = ""
quantity = ""
for word in cust_input_list:
    if word in fruitsList:
        fruit = word
    elif (word in quantityList) or (re.match(r'[0-9]',word)):
        quantity = word
if quantity == "":
    quantity = input(f"How many {fruit} you want ? ") 
print(fruit , quantity)

# OUTPUT:

# What do you want to buy? I want apple    
# How many apple you want ? 5
# apple 5
