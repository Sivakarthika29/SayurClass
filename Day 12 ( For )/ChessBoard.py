######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares
whiteTurn = True
for i in range(1, 9):
    for j in range(1, 9):
        if whiteTurn:
            print('\u25A0' , end=" ")
            whiteTurn = False
        else:
            print("B",end=" ")
            whiteTurn = True
    whiteTurn = not whiteTurn
    print()


# OUTPUT:

# ■ B ■ B ■ B ■ B 
# B ■ B ■ B ■ B ■ 
# ■ B ■ B ■ B ■ B 
# B ■ B ■ B ■ B ■ 
# ■ B ■ B ■ B ■ B 
# B ■ B ■ B ■ B ■ 
# ■ B ■ B ■ B ■ B 
# B ■ B ■ B ■ B ■ 