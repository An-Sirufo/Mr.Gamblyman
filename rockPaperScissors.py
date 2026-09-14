## Game 2: Rock Paper Scissors

def rockps():

    import random
    import time
    possible = list(range(0, 3)) 
    play_meaning = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}

    while True:
        play = input("\nRock Paper Scissorts:\nWhat will you play?\n1. Rock ✊\n2. Paper 🖐️\n3. Scissors ✌️\n4. Give up\n")
        if play in ['4', 'Give up', 'give up']:
            return
        elif not play in ['1', '2','3']:
            print("Pick 1, 2 or 3 please")
        else:
            break

    play = int(play) - 1

    time.sleep(1)
    pc_play = random.choice(possible)
    print('You picked {} and PC picked {}'.format(play_meaning[play], play_meaning[pc_play]))


    def whoWon(refplayer, otherplayer):
        ans = (int(refplayer) - int(otherplayer)) % 3
        if ans == 0:
            print("It's a Tie!")
            result = None
        elif ans == 1:
            print("You Win!")
            result = True
        else:
            print("You Lose!")
            result = False
        return result
            
    time.sleep(1)
    the_game = whoWon(play, pc_play)
    
    return the_game
rockps()