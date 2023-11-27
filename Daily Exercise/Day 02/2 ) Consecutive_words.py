''' Problem #2
Write a program that reads a passage or string and counts the occurrences of two consecutive words 
that are the same without any other specific word in between.
For example, count the occurrences of "apple apple" but not "apple orange apple." '''

passage = input("Enter the passage : ")
li = []
consecutive = dict()
word = passage.split(" ")
for i in range(len(word)):
    if i !=  len(word)-1:
        if word[i] == word[i+1]:
            li.append(f"{word[i]} {word[i+1]}")
for j in li:
    if j in consecutive:
        consecutive[j] += 1
    else:
        consecutive[j] = 1
print(consecutive)


'''
OUTPUT:

Enter the passage : apple apple and orange the the orange orange apple apple 
{'apple apple': 2, 'the the': 1, 'orange orange': 1} '''
            
    
