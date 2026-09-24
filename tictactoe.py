##Game 4: Tic Tac Toe

import time
import random

s = '\033[4m' ## for start of underline formatting
e = '\033[0m' ## for end of underline formatting

play = input("Which square will you pick?" + f'{s}' + "\n 1 | 2 | 3 \n 4 | 5 | 6 "+ f'{e}' +"\n 7 | 8 | 9 \n")
play = int(play) ##needs to make check for if number and if it's a possible play, also quit option


board_dict = {}
play_code = 1

for row in range(0,3):
    for item in range(0,3):
        board_dict.update({play_code : (row,item)})
        play_code += 1


print("Model:           Real one:\n" + f'{s}' + " 1 | 2 | 3 " + f'{e}' + "      " + f'{s}' + f'   |   |   \n 4 | 5 | 6 ' + f'{e}' + "      " + f'{s}' + "   |   |   \n" + f'{e}' + " 7 | 8 | 9          |   |   ")

##possibly make a function to make it easier to do this crazy thing
