''' Problem #1
Generate the following output using for loop. Go until g.

a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba

look at the output and find the pattern. Hint - add next letter in the alphabet in each row '''

start = 'a'
end = 'g'
str = start
print(str)
for i in range(ord(start)+1,ord(end)+1):    # 98 to 103
    str = str + chr(i) + str
    print(str)


'''
OUTPUT:

a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
'''

    

