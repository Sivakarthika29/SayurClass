''' Problem #1
Print the following pattern
1
212
32123
4321234
543212345
Get user input for how far to go (up to 0) '''

user_input = int(input("How far to go ? "))
start = 1
print(start)
for i in range(start+1,user_input+1):
    start = str(i)+str(start)+str(i)
    print(start)

'''
OUTPUT:

How far to go ? 6
1
212
32123
4321234
543212345
65432123456 '''
    