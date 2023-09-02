"""The user just bought a few things in your  shop. Ask the user what he bought.
Cost of one vadai is Rs 30, one soda is Rs20 and one sandwich is Rs 100. Calculate the total cost.
Ask the user to pay the amount. Receive the amount from the user (get money as input). 
Print the change amount you have to give to the user."""

cost_of_one_vadai=30
cost_of_one_soda=20
cost_of_one_sandwich=100
vadai_count=int(input("Number of vadai:"))
soda_count=int(input("Number of soda:"))
sandwich_count=int(input("Number of sandwich:"))
vadai_amount=float(vadai_count*cost_of_one_vadai)
soda_amount=float(soda_count*cost_of_one_soda)
sandwich_amount=float(sandwich_count*cost_of_one_sandwich)
total_amount=vadai_amount+soda_amount+sandwich_amount
print("Total amount=",total_amount)

# OUTPUT:

# Number of vadai:4
# Number of soda:1
# Number of sandwich:3
# Total amount= 440.0