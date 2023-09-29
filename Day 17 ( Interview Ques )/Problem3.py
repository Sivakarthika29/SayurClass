''' 3. Accept 2 integers. print all nos which are mirror nos falling 
between the range.
eg: first no 300
 second no 400
303,313,323.......393 

try to incorporate error handling feature too in all the 
above problems. '''


mirror_no = []
first_no = 300
second_no = 400

while first_no <= second_no:
    reversed_no = str(first_no)[::-1]
    if first_no == int(reversed_no):
        mirror_no.append(first_no)
    first_no += 1
print(f"Mirror Numbers : {mirror_no}")

# OUTPUT:

# Mirror Numbers : [303, 313, 323, 333, 343, 353, 363, 373, 383, 393]
