''' problem #4
write a program to find if two strings are same.
two string are considered same if both strings have same letters in same order, but from different starting point
eg abcd is same as bcda (a is moved to the right)
abcd is same as cdab 
abcd is not same as cdba

123456 = 456123
123456 not = 412356
hint - 
there are many simple answers. you can try with slice function '''

is_same = True
string_1 = input("Enter the String 1 : ")
string_2 = input("Enter the String 2 : ")
if (len(string_1) == len(string_2)):
    y = string_1.index(string_2[0])
    for i in range(len(string_1)):
        if (y != len(string_1)-1):
            if (string_1[y] == string_2[i]):
                y += 1
            else:
                is_same = False
                break
        else:
            y = 0
    if(is_same):
        print(f"{string_1} is same as {string_2}")
    else:
        print(f"{string_1} is not same as {string_2}")
else:
    print(f"{string_1} is not same as {string_2}")
    exit(0)

''' 
OUTPUT:

Enter the String 1 : abcd
Enter the String 2 : acbd
abcd is not same as acbd

Enter the String 1 : 123456
Enter the String 2 : 456123
123456 is same as 456123

Enter the String 1 : abcd
Enter the String 2 : cdab
abcd is same as cdab
'''

