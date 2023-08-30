"""Program to find out how many Kg of onion or tomato we can buy.
One Kg of Onion is 20rs, Tomato is 10.5rs.  Input is the budget."""

one_kg_of_onion=20
one_kg_of_tomato=10.5
budget=float(input("Enter your budget:"))
print("1.Onion\n2.Tomato")
option=int(input("Enter your option:"))
if option == 1:
    budget_onion=float(budget/one_kg_of_onion)
    print(budget_onion,"Kg of onion we can buy in your budget.")
elif option == 2:
    budget_tomato=float(budget/one_kg_of_tomato)
    rounded_budget_tomato=round(budget_tomato,1)              #round() syntax:round(number,digits)
    print(rounded_budget_tomato,"Kg of tomato we can buy in your budget.")
else:
    print("Please enter correct option")
