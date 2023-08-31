def check_letter(word,letter):
    for i in range(0,len(word)):
        if letter == word[i]:
            return True
    return False
name=input("Enter a word")
word=""
for i in range(0,len(name)):
    count=0
    if not check_letter(word,name[i]):
        word=word+name[i]
        for j in range(i,len(name)):
            if name[i]==name[j]:
                count=count+1
        print(f"{name[i]} has present in the word is {count} times")
    else:
        continue 
