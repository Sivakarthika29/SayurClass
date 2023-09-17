######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.

#      1  2  3  4  5
#   ********************
# 1 |  1  2  3  4  5
# 2 |  2  4  6  8 10
# 3 |  3  6  9 12 15
# 4 |  4  8 12 16 20
# 5 |  5 10 15 20 25

start = int(input("Enter the start value : "))
end = int(input("Enter the end value : "))


for i in range(start,end+1):
    print(f"\t{i}",end =  "  ")

print("\n   ",end="")
print("*" * end*8)

for i in range(start, end+1):
    print(f"{i}  |  ",end="\t")
    for j in range(start, end+1):
        print(f"{i*j}",end="\t")
    print("")

# OUTPUT:

# Enter the start value : 1
# Enter the end value : 5
#         1       2       3       4       5  
#    ****************************************
# 1  |    1       2       3       4       5
# 2  |    2       4       6       8       10
# 3  |    3       6       9       12      15
# 4  |    4       8       12      16      20
# 5  |    5       10      15      20      25