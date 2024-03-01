 #Input is a sentence. Find the number of times each word appears.

sentence=input("Enter the sentence:")
all_freq = dict()
txt = sentence.split(" ")                        
 
for i in txt:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("Number of times each word is :\n "+ str(all_freq))



# OUTPUT:

# Enter the sentence:my name is siva my father name is sekar
# Number of times each word is :
# {'my': 2, 'name': 2, 'is': 2, 'siva': 1, 'father': 1, 'sekar': 1}