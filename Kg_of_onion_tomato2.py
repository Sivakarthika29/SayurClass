#7.Program to find out how many Kg of onion or tomato we can buy. One Kg of Onion is 20rs, Tomato is 10.5rs.  Input is the budget. 
#7.1 Same as above, but the price of Onion is different based on the city. Chennai - Rs30, Trichy Rs27, Madurai Rs 34. Input is budget and city.
#7.2 Same as above, but add 3% of the budget for petrol expenses. 

one_kg_of_tomato=10.5
budget=float(input("Enter your budget:"))
budget=budget-((3/100)*budget)
one_kg_of_chennai_onion=30
one_kg_of_trichy_onion=27
one_kg_of_madurai_onion=34
print("1.Tomato\n2.Chennai_onion\n3.Trichy_onion\n4.Madurai_onion")
option=int(input("Enter your option:"))
if option==1:
    budget_tomato=float(budget/one_kg_of_tomato)
    rounded_budget_tomato=round(budget_tomato,1)               #round() syntax:round(number,digits)
    print(rounded_budget_tomato,"Kg of tomato we can buy in your budget.")
elif option==2:
    budget_chennai_onion=float(budget/one_kg_of_chennai_onion)
    rounded_budget_chennai_onion=round(budget_chennai_onion,1) 
    print("In chennai",rounded_budget_chennai_onion,"Kg of onion we can buy in your budget.")
elif option==3:
    budget_trichy_onion=float(budget/one_kg_of_trichy_onion)
    rounded_budget_trichy_onion=round(budget_trichy_onion,1) 
    print("In trichy",rounded_budget_trichy_onion,"Kg of onion we can buy in your budget.")
elif option==4:
    budget_madurai_onion=float(budget/one_kg_of_madurai_onion)
    rounded_budget_madurai_onion=round(budget_madurai_onion,1) 
    print("In madurai",rounded_budget_madurai_onion,"Kg of onion we can buy in your budget.")
else:
    print("Please enter correct option") 