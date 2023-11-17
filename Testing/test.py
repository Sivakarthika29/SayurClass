
# When the cumulative bonus is more than one lakh , base salary is increased
#     by 5% for each month. Calculate the salary for each month.
monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12] 
basePay = 10000
previousMonthSalary = 0

for month, phoneCount in enumerate(monthlySalesList):
    bonus = 0
    if phoneCount >= 5:
        bonus += 5000
        if bonus >= 100000:
            currentMonthSalary = basePay +basePay*5/100
        print (f"This month's salary before additional bonus {currentMonthSalary}") 
