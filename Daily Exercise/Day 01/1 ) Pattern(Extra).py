''' Problem #1
Generate the following output using for loop. Go until g.

a
a-b-a
aba-c-aba
abacaba-d-abacaba
abacabadabacaba-e-abacabadabacaba
abacabadabacabaeabacabadabacaba-f-abacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba-g-abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba

look at the output and find the pattern. Hint - add next letter in the alphabet in each row '''


start = 'a'
end = 'g'
print(start)
for i in range(ord(start)+1,ord(end)+1):
    print(f"{start}-{chr(i)}-{start}")
    start = start + chr(i) + start

''' OUTPUT:

a
a-b-a
aba-c-aba
abacaba-d-abacaba
abacabadabacaba-e-abacabadabacaba
abacabadabacabaeabacabadabacaba-f-abacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba-g-abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba '''
    
    