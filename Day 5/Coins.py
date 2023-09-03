"""You have three types of coins , values of 1, 3 and 5
given a number, you need to find minimum coins required. 
eg., if input is 8 - answers 5(1), 3(1) - 2 coins 
if input is 10 - answer is 5(2) - 2 coins
if input is 4 - answer is 3(1), 1(1) - 2 coins
if input is 17 - answers is 5(3), 1(2) - 5 coins"""

coin1 = 0
coin3 = 0 
coin5 = 0 
amount = int(input("Enter your amount : ")) 
total_coins = 0 
while amount >= 5:
     amount = amount - 5 
     coin5 += 1 
     total_coins += 1 
while amount >= 3:
     amount = amount - 3 
     coin3 += 1 
     total_coins += 1
while amount >= 1: 
    amount = amount - 1
    coin1 = coin1 + 1 
    total_coins += 1 
print(f"We need {total_coins} coins") 
if coin1 != 0: 
     print(f"1rs coins = {coin1}") 
if coin3 != 0:
    print(f"3rs coins = {coin3}") 
if coin5 != 0: 
    print(f"5rs coins = {coin5}")


# OUTPUT:

# Enter your amount : 8
# We need 2 coins
# 3rs coins = 1  
# 5rs coins = 1  









