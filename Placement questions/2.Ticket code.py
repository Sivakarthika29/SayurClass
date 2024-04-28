letter = "ABABABB"
for i in range(2,len(letter),2):
    if letter[i] != letter[0]:
        print("NO")
        exit()
print("Yes")
exit()

for j in range(3,len(letter),2):
    if letter[j] != letter[1]:
        print("NO")
        exit()
print("Yes")




        