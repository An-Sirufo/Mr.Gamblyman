## Game 2: Rock Paper Scissors

import random
possible = ['1','2','3']

while True:
    play = input("What will you play?\n1. Rock ✊\n2. Paper 🖐️\n3. Scissors ✌️\n4. Quit\n")
    if play == '4':
        quit()
    elif not play in possible:
        print("Pick 1, 2 or 3 please")
    else:
        break

pc_play = random.choice(possible)
print(pc_play)
res = (int(play) - int(pc_play)) % 3
print(res)

""" if play == pc_play:
    print("It's a tie!")
elif: """
