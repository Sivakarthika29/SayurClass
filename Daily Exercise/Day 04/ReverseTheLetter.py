''' Problem #1
write a program that reads a passage and reverses the order of 
letters in each word while keeping the word order intact. Use function.
Eg- input - I am Sayur
Output I ma ruyaS '''


def reverseTheLetters(aString):
    reversed_ans = []
    for letter in aString:
        reverse_word = (letter)[::-1]
        reversed_ans.append(reverse_word)
    print(" ".join(reversed_ans))

myString = input("Input a string : ").split(" ")
reverseTheLetters(myString)


''' OUTPUT:

Input a string : I am Sayur
I ma ruyaS '''
