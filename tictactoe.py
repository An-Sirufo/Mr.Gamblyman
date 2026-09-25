##Game 4: Tic Tac Toe

import time
import random

s = '\033[4m' ## for start of underline formatting
e = '\033[0m' ## for end of underline formatting

board_dict = {}
board_coord = []
play_code = 1

for row in range(0,3):
    board_coord.append([])
    for item in range(0,3):
        board_dict.update({play_code : (row,item)})
        board_coord[row].append(play_code)
        play_code += 1


def board(coord):
    return f'{s}' + f" {coord[0][0]} | {coord[0][1]} | {coord[0][2]} \n {coord[1][0]} | {coord[1][1]} | {coord[1][2]} "+ f'{e}' + f"\n {coord[2][0]} | {coord[2][1]} | {coord[2][2]} \n"

play = input("Which square will you pick?\n" + board(board_coord))
while True:
    if play.isdigit():
        play = int(play)
    else:
        play = input("Please write a number between 1 and 9\n")
    if not play in range(1,10):
        play = input("Please write a number between 1 and 9\n")
    else:
        break


def update_board(play): #hmmmmmmmmm should I make it print here?? there's 2 fuctions for updating the board now....
    x, y = board_dict[play]
    board_coord[x][y] = "X"
    print(board(board_coord))

pc_play = random.choice(range(1,10))
print(pc_play)