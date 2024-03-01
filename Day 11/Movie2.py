############## Problem 2 ################
#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.

totalMoney = 0 
limit = 5
for i in range (1,limit+1):
    money = int(input("How much money do your parents give you? "))
    if money < 10:
        continue
    totalMoney = totalMoney + money
    print(f"I got {totalMoney} Rupees\nThank you!!!")
    if money >= 1000:
        break

# OUTPUT:

# How much money do your parents give you? 56
# I got 56 Rupees
# Thank you!!!
# How much money do your parents give you? 500
# I got 556 Rupees
# Thank you!!!
# How much money do your parents give you? 8
# How much money do your parents give you? 100
# I got 656 Rupees
# Thank you!!!
# How much money do your parents give you? 50
# I got 706 Rupees
# Thank you!!!    