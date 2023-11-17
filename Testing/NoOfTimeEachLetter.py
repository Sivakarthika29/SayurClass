 #Input is a sentence. Find the number of times each letter appears.

sentence=input("Enter the sentence:")
all_freq = {}                          # key : value
 
for i in sentence:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("Number of times each word is :\n "+ str(all_freq))



# OUTPUT:

# Enter the sentence:sivakarthika
# Number of times each word is :
#  {'s': 1, 'i': 2, 'v': 1, 'a': 3, 'k': 2, 'r': 1, 't': 1, 'h': 1}