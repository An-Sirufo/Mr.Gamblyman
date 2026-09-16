##Game3: Dice Duel

import random
import time

def dduel():

    di_name = {1: '1 ⚀', 2: '2 ⚁', 3: '3 ⚂', 4: '4 ⚃', 5: '5 ⚄', 6: '6 ⚅'}
    
    while True:
        style = input("How will you roll your dice?\n1. With determination\n2. With love\n3. Like a coin\n4. Give up\n")
        if not style in ['1','2','3','4']: 
            print("Pick 1, 2, 3 or 4, please.")
        elif style in ['4', 'Give up', 'give up']:
            return
        else:
            break
    
    di1, di2 = random.randint(1, 6), random.randint(1, 6)
    player_sum = di1 + di2

    def styling(dice, off_range, offset):
        if dice in off_range:
            dice += random.randint(*offset)
        return dice

    if style == '1':
        di1, di2 = styling(di1, range(3, 5), (-2, 2)), styling(di2, range(3, 5), (-2, 2))
    elif style =='2':
        di1, di2 = styling(di1, range(1, 2), (0, 2)), styling(di2, range(1, 2), (0, 2))
        di1, di2 = styling(di1, range(5, 6), (-2, 0)), styling(di2, range(5, 6), (-2, 0))

    pcdi1, pcdi2 = random.randint(1, 6), random.randint(1, 6)
    pc_sum = pcdi1 + pcdi2

    player_sum = di1 + di2

    print('rolling the dice.............')
    time.sleep(1)
    print("Your dice roll resulted in {} and {}, a sum of {}".format(di_name[di1], di_name[di2], player_sum))
    time.sleep(0.5)
    print("PC's dice roll resulted in {} and {}, a sum of {}".format(di_name[pcdi1], di_name[pcdi2], pc_sum))
    time.sleep(1)

    if player_sum == pc_sum:
        print("It's a tie! You both had the same results!")
        result = None
    elif player_sum > pc_sum:
        print("You win! Your sum was bigger than PC's.")
        result = True
    else:
        print("You lose! Your sum was lower than PC's, not your lucky day ;)")
        result = False

    return result