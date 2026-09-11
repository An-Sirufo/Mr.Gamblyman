## Game 2: Rock Paper Scissors

import random
import time
possible = ['0','1','2']
play_meaning = {'0': 'Rock', '1': 'Paper', '2': 'Scissors'}

while True:
    play = input("What will you play?\n0. Rock ✊\n1. Paper 🖐️\n2. Scissors ✌️\n3. Quit\n")
    if play in ['3', 'Quit', 'quit']:
        quit()
    elif not play in possible:
        print("Pick 0, 1 or 2 please")
    else:
        break

time.sleep(1)
pc_play = random.choice(possible)
print('You picked {} and PC picked {}'.format(play_meaning[play], play_meaning[pc_play]))

def whoWon(refplayer, otherplayer):
    ans = (int(refplayer) - int(otherplayer)) % 3
    if ans == 0:
        print("It's a Tie!")
    elif ans == 1:
        print("You Win!")
    else:
        print("You Lose!")
        
time.sleep(1)
the_game = whoWon(play, pc_play)


