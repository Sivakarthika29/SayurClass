coffee_quantity, tea_quantity, vadai_quantity = 30 , 25 , 50
coffee_amount, tea_amount, vadai_amount = 15 , 10 , 8
tea_cost, coffee_cost, vadai_cost= 0 , 0 , 0
coffeeProfit, teaProfit, vadaiProfit = 4 , 2 , 3
totalCoffeeProfit, totalTeaProfit, totalVadaiProfit = 0, 0, 0
while(True):
    choice = int(input("Enter 1.Coffe 2.Tea 3.Vadai "))
    if choice == 1:
        coffee_order = int(input("Enter no of Coffee : "))
        coffee_cost = coffee_order * coffee_amount
        coffee_quantity -= coffee_order 
        totalCoffeeProfit += coffeeProfit
    if choice == 2:
        tea_order = int(input("Enter no of Tea : "))
        tea_cost = tea_order * tea_amount
        tea_quantity -= tea_order
        totalCoffeeProfit += teaProfit
    if choice == 3:
        vadai_order = int(input("Enter no of Vadai : "))
        vadai_cost = vadai_order * vadai_amount
        vadai_quantity -= vadai_order
        totalVadaiProfit += vadaiProfit
    total_amount = coffee_cost + tea_cost + vadai_cost
    totalProfit = totalCoffeeProfit + totalCoffeeProfit + totalVadaiProfit
    print(f"You spent amount : {total_amount}")
    break