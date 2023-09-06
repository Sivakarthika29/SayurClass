"""Get two names. If the length of the two names is not equal, add 'a' at the end of the short name
    until the length is equal. 
    Eg - input - cat, arrow. (legnth is not equal) 
    Output - cataa, arrow (length is equal by adding a)"""

name_1=input("Enter the first name:")
name_2=input("Enter the second name:")
while len(name_1) != len(name_2):
    if len(name_1) <= len(name_2):
        name_1=name_1+'a'
        ans = name_1
    else:
        name_2=name_2+'a'
        ans = name_2
print(ans)
print(name_1,",",name_2,"length is equal")


# OUTPUT:

# Enter the first name:cat
# Enter the second name:arrow
# cataa
# cataa , arrow length is equal