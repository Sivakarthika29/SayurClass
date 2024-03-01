''' Problem #2
Read a passage from a file. 
Count the number of times the word 'the' followed by another 'the' without 'a' in between.
Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.
answer is 4 (The king, the forest, The King the next). '''

ans = []
try:
    input_file = open('SayurClass/Daily Exercise/Day 03/input_text.txt','r')
    passage = input_file.read()
except FileNotFoundError:
    print("File Not Found")
finally:
    input_file.close()
print(passage)

split_pass = passage.split(" ")
for i in range(len(split_pass)):
    if split_pass[i] == "The" or split_pass[i] == "the":
        ans.append(f"{split_pass[i]} {split_pass[i+1]}")
    elif split_pass[i] == "A" or split_pass[i] == "a":
        ans.pop()
print(f"Answer is {len(ans)} {ans}")

''' OUTPUT: 

The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.
Answer is 5 ['The king', 'the forest', 'The king', 'the forest', 'the next'] '''


