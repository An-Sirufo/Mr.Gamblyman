import time
import highCard
import rockPaperScissors

dub = 10

def dub_name(dub):
    if dub in range(-2,2):
        return "{} Doubloon".format(dub)
    else:
        return "{} Doubloons".format(dub)

print("Hello! I'm Mr. Gamblyman, I'll be your host tonight.")
time.sleep(1)
print("You start with {}, your job is to multiply this using only your LUCK.".format(dub_name(dub)))
time.sleep(1)

will = True

while will == True:

    while True:
        choice = input("What do you want to play now?\n1. High Card\n2. Rock Paper Scissors\nQuit\n")
        if not choice in ['1', '2', 'quit', 'Quit', 'q']:
            time.sleep(0.5)
            print("Please pick a number or type 'quit' to quit")
        else:
            break

    if choice in ['quit', 'Quit', 'q']:
        quit()
    else:
        while True:
            bet = input("How much will you bet? You have {}.\n".format(dub_name(dub)))
            if not bet.isdigit():
                print("Pick a number, please")
            elif int(bet) > dub:
                print("You're not that rich, buddy")
            else:
                break
    
    bet = int(bet)

    ##plays games
    if choice == '1':
        result = highCard.highC()
    elif choice == '2':
        result = rockPaperScissors.rockps()

    if result == 1: ##win
        dub += bet
        print("Congrats! You win {}, so now you have {}.".format(dub_name(bet), dub_name(dub)))
    elif result == 0: ##lose
        dub -= bet
        print("Oh man! You lost {}, so now you have {}".format(dub_name(bet),dub_name(dub)))
    else: ##tie
        print("Since you tied, nothing changes with your Doubloons")

    will = False

    time.sleep(1.5) 
    if dub == 0:
        print("GAME OVER! You're poor as a rat now!\npew pew get shot and die ᡕᠵデᡁ᠊╾━-----💥") 
    else:
        while True:
            will = input("Wanna keep going?(Y/N)\n")
            if not will in ['n','N','No','no','quit', 'y', 'Y', 'yes', 'Yes', 'yis']:
                print('Please pick y (yes) or n (no)')
            else:
                break
    
    if will in ['y', 'Y', 'yes', 'Yes', 'yis']:
        will = True
