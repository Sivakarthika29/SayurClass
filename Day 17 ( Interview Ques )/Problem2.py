''' Problem 2
2. From a given passage find the longest and shortest word 
and print the same. Accept the passage as an input from user '''

passage = input("Enter the passage : ")
split_passage= passage.split(" ")
longest = max(split_passage , key =len)
shortest = min(split_passage , key =len)
print(f"Longest word : {longest}")
print(f"Shortest word : {shortest}")



# OUTPUT:

# Enter the passage : I am Sivakarthika
# Longest word : Sivakarthika
# Shortest word : I