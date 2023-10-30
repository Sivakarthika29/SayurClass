def max1(l1):
    if len(l1)==1:
        return l1[0]
    else:
        return(max(l1[0],max1(l1[1:])))

l1= [2,10,20,100]
max_val=max1(l1)
print(max_val)

# OUTPUT:

# 100