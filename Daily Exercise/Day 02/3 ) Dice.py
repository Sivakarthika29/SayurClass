''' Problem #3
Its is a single player game where the user starts with 0 points. User keeps rolling the 
dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
added. If the number is odd, then if the number is 1,3 then the user has to jump. 
If the number is 5, then 3 points are added. The game ends when the user has 50 points.'''

import random
points = 0
winning_points = 50
while points < winning_points:
    dice_list = [0, 1, 2, 3, 4, 5, 6]                    # Another method(There is no need to define the list.)
    random_no = random.choice(dice_list)                 # random_no = random.randint(0, 6)
    print(f"Your points are {points}")
    print(f"Rolled no : {random_no}")
    
    if random_no == 0:
        print("GAME END")
        break
    elif random_no % 2 == 0:
        points += 2
        print(f"2 Points are added")
    elif (random_no == 1) or (random_no == 3):
        continue
    else:
        points += 3
        print(f"3 Points are added")
else:
    print("Your reached the winning points.So, the game was end.")

'''
OUTPUT:

Your points are 0
Rolled no : 5
3 Points are added
Your points are 3
Rolled no : 6
2 Points are added
Your points are 5
Rolled no : 2
2 Points are added
Your points are 7
Rolled no : 1
Your points are 7
Rolled no : 0
GAME END '''