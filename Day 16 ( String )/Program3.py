''' 3. Write the function mostFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated the same), 
returns a lowercase string containing the letters of s in most frequently used order. (In the event of a tie between two letters, 
follow alphabetic order.)
Eg - "We Attack at Dawn" is input. Output should be 'atwcdekn'
Do not use dictionaries. Try to use string built in functions. '''

str_input = input("Enter the String : ")                             # We Attack at Dawn
lowerCase = str_input.casefold()                                          # we attack at dawn
removeSpace = lowerCase.replace(" ","")                         # weattackatdawn
sorted_list = sorted(removeSpace)                        # ['a', 'a', 'a', 'a', 'c', 'd', 'e', 'k', 'n', 't', 't', 't', 'w', 'w']

count_list = []
for i in range(len(sorted_list)):
    count_list.append(sorted_list.count(sorted_list[i]))        #  [4, 4, 4, 4, 1, 1, 1, 1, 1, 3, 3, 3, 2, 2]

merge_list = list(zip(count_list,sorted_list))       # [(4, 'a'), (4, 'a'), (4, 'a'), (4, 'a'), (1, 'c'), (1, 'd'), (1, 'e'), (1, 'k'),(1, 'n'), (3, 't'), (3, 't'), (3, 't'), (2, 'w'), (2, 'w')]

sorted_merge_list = sorted(merge_list,reverse=True)  # [(4, 'a'), (4, 'a'), (4, 'a'), (4, 'a'), (3, 't'), (3, 't'), (3, 't'), (2, 'w'), (2, 'w'), (1, 'n'), (1, 'k'), (1, 'e'), (1, 'd'), (1, 'c')]

unique_list = []
for tup in sorted_merge_list:
    if tup in unique_list:
        continue
    unique_list.append(tup)            # [(4, 'a'), (3, 't'), (2, 'w'), (1, 'n'), (1, 'k'), (1, 'e'), (1, 'd'), (1, 'c')]


final_result = ""  # twcdekn
temp = ""  # a
num = unique_list[-1][0]
for tup_index in reversed(range(len(unique_list))):
    freq , letter = unique_list[tup_index]
    if freq == num:
        temp = temp + letter
        continue
    num = freq
    final_result = temp + final_result
    temp = letter
final_result = temp + final_result
print(final_result)

# OUTPUT:

# Enter the String : We Attack at Dawn
# atwcdekn