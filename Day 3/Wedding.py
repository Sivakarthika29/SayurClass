"""Calculate wedding expenses. Cost for lunch per person is Rs200. Cost for Breakfast per
 person is half of lunch cost. Cost of the hall is Rs 200 per person.
  Decoration is 50% of Hall cost. Parking is 10% of the Hall cost. 
  Decide what should be the input and calculate the cost."""

lunch_cost_per_person=200
breakfast_cost_per_person=lunch_cost_per_person/2
hall_cost_per_person=200
no_of_person=int(input("Enter the number of person:"))
total_lunch_cost=lunch_cost_per_person*no_of_person
total_breakfast_cost=breakfast_cost_per_person*no_of_person
total_hall_cost=hall_cost_per_person*no_of_person
decoration=total_hall_cost/2
parking_cost=10*total_hall_cost/100
print("Total lunch cost:",total_lunch_cost)
print("Total breakfast cost:",total_breakfast_cost)
print("Total hall cost:",total_hall_cost)
print("Decoration cost:",decoration)
print("Parking cost:",parking_cost)

