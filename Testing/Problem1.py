""" You have a message that you want to send to your friend. You don't want others 
to see the message. You code the message and send it. The alg to code is - split each 
word in half and reverse it (eg cricket becomes ketccri), if the word ends with a vowel,
split at the last letter and reverse (eg cinema becomes acinem), if the word has
numbers, spell the number but add A as first and last letters """

userInput = "karthika"
res = ""
last_ele = (userInput[len(userInput)-1])
if last_ele == 'a' or last_ele == 'e' or last_ele == 'i' or last_ele =='o' or last_ele =='u':
    for i in range(len(userInput)-1):
        res = res + userInput[i]
    print(last_ele + res)
else:
    half = len(userInput)//2
    for j in range(half+1 , len(userInput)):
        res = res + userInput[j]
    for i in range(half+1):
        res = res + userInput[i]
    print(res)