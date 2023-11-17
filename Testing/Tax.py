incomeSlabs = [300000,600000,900000,1200000,1500000]
taxPercentage = [0.05, 0.1, 0.15, 0.2, 0.3]
previousTax = [0, 15000, 45000, 90000, 150000]
salary = int(input("Enter your salary: "))
for i in range(0,len(incomeSlabs)):
    if salary <= incomeSlabs[i]:
        if i == 0:
            tax = salary*taxPercentage[i]
        else:
            tax = (salary - incomeSlabs[i-1])*taxPercentage[i]
            print(taxPercentage[i])
        break
