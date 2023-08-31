 #Input is a sentence. Find the number of times each word appears.

sentence=input("Enter the sentence:")
all_freq = {}
 
for i in sentence:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("Number of times each word is :\n "+ str(all_freq))

