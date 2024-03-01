''' Problem #3
From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
for each word. Write this information at the end of file under the heading "Summary of 4 letter words"

For problem 2 and 3,
Make sure your code includes exception handling for reading from a file.
Reading material for exception handling - https://www.w3schools.com/python/python_try_except.asp
Video https://youtu.be/83Y2qZvWxdE?si=g2MB45bZHI8-ah5q '''

li = []
noOfOccurrences = {}
try:
    input_file = open('SayurClass/Daily Exercise/Day 03/input_text.txt','r')
    passage = input_file.read()
    print(passage)

    split_pass = passage.split(" ")
    for i in range(len(split_pass)):
        if len(split_pass[i]) == 4:
            li.append(split_pass[i])

    for j in li:
        if j in noOfOccurrences:
            noOfOccurrences[j] += 1
        else:
            noOfOccurrences[j] = 1
    print(noOfOccurrences)

except FileNotFoundError:
    print("File Not Found")
finally:
    input_file.close()


''' OUTPUT:

The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.
{'king': 3, 'went': 2, 'with': 1, 'wife': 1, 'shot': 1, 'next': 1, 'day.': 1} '''