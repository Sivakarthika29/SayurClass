''' Problem #2
You have 6 x 6 game board where each cell is shown as a *
This is a two player dice game. The die has numbers 1 to 6.
Each player rolls the dice twice. First roll is row number, second roll is col number.
After the player rolls the dice, in the (row,col) enter the player's initial. 
If the player  A rolls the dice and  if  player B already has their initial in the same row,col
add a point to A and change the initial to A. 

Player who gets 5 points first wins the game.
Print the board each time after the user rolls and also print the current score.
Use functions '''

import random

game_board = [["*","*","*","*","*","*"],
              ["*","*","*","*","*","*"],
              ["*","*","*","*","*","*"],
              ["*","*","*","*","*","*"],
              ["*","*","*","*","*","*"],
              ["*","*","*","*","*","*"]]

def display_board():
    print()
    for row in game_board:
        for col in row:
            print(col , end = " ")
        print()
    print()

player_A_points , player_B_points = 0 , 0
winning_points = 5

while(player_A_points < winning_points and player_B_points < winning_points):
    input("Player A turn , enter to roll the dice ")
    row = random.randint(1,6)
    col = random.randint(1,6)
    print(f"Row {row} , Col {col}")
    if game_board[row-1][col-1] == "B":
        player_A_points += 1
        game_board[row-1][col-1] = "A"
    else:
        game_board[row-1][col-1] = "A"

    input("Player B turn , enter to roll the dice ")
    row = random.randint(1,6)
    col = random.randint(1,6)
    print(f"Row {row} , Col {col}")
    if game_board[row-1][col-1] == "A":
        player_B_points += 1
        game_board[row-1][col-1] = "B"
    else:
        game_board[row-1][col-1] = "B"

    display_board()
    print("Player A points - ",player_A_points)
    print("Player B points - ",player_B_points)


if player_A_points == winning_points:
    print("***** PLAYER A WON *****")
else:
    print("***** PLAYER B WON *****")

''' OUTPUT:

Player A turn , enter to roll the dice 
Row 6 , Col 3
Player B turn , enter to roll the dice 
Row 3 , Col 6

* * * * * * 
* * * * * * 
* * * * * B 
* * * * * * 
* * * * * * 
* * A * * * 

Player A points -  0
Player B points -  0
Player A turn , enter to roll the dice
Row 4 , Col 4
Player B turn , enter to roll the dice
Row 3 , Col 4

* * * * * *
* * * * * *
* * * B * B
* * * A * *
* * * * * *
* * A * * *

Player A points -  0
Player B points -  0
Player A turn , enter to roll the dice
Row 3 , Col 6
Player B turn , enter to roll the dice
Row 3 , Col 2

* * * * * *
* * * * * *
* B * B * A
* * * A * *
* * * * * *
* * A * * *

Player A points -  1
Player B points -  0
Player A turn , enter to roll the dice
Row 1 , Col 4
Player B turn , enter to roll the dice
Row 4 , Col 2

* * * A * *
* * * * * *
* B * B * A
* B * A * *
* * * * * *
* * A * * *

Player A points -  1
Player B points -  0
Player A turn , enter to roll the dice
Row 3 , Col 1
Player B turn , enter to roll the dice
Row 3 , Col 6

* * * A * *
* * * * * *
A B * B * B
* B * A * *
* * * * * *
* * A * * *

Player A points -  1
Player B points -  1
Player A turn , enter to roll the dice
Row 5 , Col 6
Player B turn , enter to roll the dice
Row 2 , Col 4

* * * A * *
* * * B * *
A B * B * B
* B * A * *
* * * * * A
* * A * * *

Player A points -  1
Player B points -  1
Player A turn , enter to roll the dice
Row 3 , Col 2
Player B turn , enter to roll the dice
Row 3 , Col 1

* * * A * *
* * * B * *
B A * B * B
* B * A * *
* * * * * A
* * A * * *

Player A points -  2
Player B points -  2
Player A turn , enter to roll the dice
Row 2 , Col 1
Player B turn , enter to roll the dice
Row 2 , Col 3

* * * A * *
A * B B * *
B A * B * B
* B * A * *
* * * * * A
* * A * * *

Player A points -  2
Player B points -  2
Player A turn , enter to roll the dice
Row 3 , Col 5
Player B turn , enter to roll the dice
Row 6 , Col 5

* * * A * *
A * B B * *
B A * B A B
* B * A * *
* * * * * A
* * A * B *

Player A points -  2
Player B points -  2
Player A turn , enter to roll the dice
Row 6 , Col 5
Player B turn , enter to roll the dice
Row 5 , Col 5

* * * A * *
A * B B * *
B A * B A B
* B * A * *
* * * * B A
* * A * A *

Player A points -  3
Player B points -  2
Player A turn , enter to roll the dice
Row 1 , Col 1
Player B turn , enter to roll the dice
Row 5 , Col 3

A * * A * *
A * B B * *
B A * B A B
* B * A * *
* * B * B A
* * A * A *

Player A points -  3
Player B points -  2
Player A turn , enter to roll the dice
Row 2 , Col 3
Player B turn , enter to roll the dice
Row 3 , Col 6

A * * A * *
A * A B * *
B A * B A B
* B * A * *
* * B * B A
* * A * A *

Player A points -  4
Player B points -  2
Player A turn , enter to roll the dice
Row 3 , Col 3
Player B turn , enter to roll the dice
Row 3 , Col 6

A * * A * *
A * A B * *
B A A B A B
* B * A * *
* * B * B A
* * A * A *

Player A points -  4
Player B points -  2
Player A turn , enter to roll the dice
Row 2 , Col 1
Player B turn , enter to roll the dice
Row 6 , Col 4

A * * A * *
A * A B * *
B A A B A B
* B * A * *
* * B * B A
* * A B A *

Player A points -  4
Player B points -  2
Player A turn , enter to roll the dice
Row 4 , Col 4
Player B turn , enter to roll the dice
Row 4 , Col 3

A * * A * *
A * A B * *
B A A B A B
* B B A * *
* * B * B A
* * A B A *

Player A points -  4
Player B points -  2
Player A turn , enter to roll the dice
Row 1 , Col 2
Player B turn , enter to roll the dice
Row 2 , Col 1

A A * A * *
B * A B * *
B A A B A B
* B B A * *
* * B * B A
* * A B A *

Player A points -  4
Player B points -  3
Player A turn , enter to roll the dice
Row 5 , Col 4
Player B turn , enter to roll the dice
Row 3 , Col 2

A A * A * *
B * A B * *
B B A B A B
* B B A * *
* * B A B A
* * A B A *

Player A points -  4
Player B points -  4
Player A turn , enter to roll the dice
Row 1 , Col 6
Player B turn , enter to roll the dice
Row 1 , Col 5

A A * A B A
B * A B * *
B B A B A B
* B B A * *
* * B A B A
* * A B A *

Player A points -  4
Player B points -  4
Player A turn , enter to roll the dice
Row 1 , Col 5
Player B turn , enter to roll the dice
Row 2 , Col 2

A A * A A A
B B A B * *
B B A B A B
* B B A * *
* * B A B A
* * A B A *

Player A points -  5
Player B points -  4
***** PLAYER A WON ***** '''