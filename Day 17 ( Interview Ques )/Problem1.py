''' 1. From a given passage extract unique words and print them.
Accept the passage as an input from the user '''

passage = input("Enter the passage : ")
split_passage= passage.split(" ")

count = 0
unique_words = []
for word in split_passage:
    for i in range (len(split_passage)):
        if word == split_passage[i]:
            count += 1
    if count == 1:
        unique_words.append(word)
        count = 0
    else:
        count = 0
print(f"Unique Words {unique_words}")

# OUTPUT:

# Enter the passage : siva karthika siva ranjani siva shankar
# Unique Words ['karthika', 'ranjani', 'shankar']