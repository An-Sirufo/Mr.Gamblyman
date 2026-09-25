import time
import highCard
import rockPaperScissors
import diceDuel

dub = 10

def dub_name(dub):
    if dub in range(-2,2):
        return f"{dub} Doubloon"
    else:
        return f"{dub} Doubloons"

print("Hello! I'm Mr. Gamblyman, I'll be your host tonight.")
time.sleep(1)
print(f"You start with {dub_name(dub)}, your job is to multiply this using only your LUCK.")
time.sleep(1)

will = True

while will == True:

    while True:
        choice = input("What do you want to play now?\n1. High Card\n2. Rock Paper Scissors\n3. Dice Duel\nQuit\n")
        if not choice in ['1', '2', '3', 'quit', 'Quit', 'q']:
            time.sleep(0.5)
            print("Please pick a number or type 'quit' to quit")
        else:
            break

    if choice in ['quit', 'Quit', 'q']:
        quit()
    else:
        while True:
            bet = input(f"How much will you bet? You have {dub_name(dub)}.\n")
            if not bet.isdecimal():
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
    elif choice == '3':
        result = diceDuel.dduel()

    if result == 1: ##win
        dub += bet
        print(f"Congrats! You win {dub_name(bet)}, so now you have {dub_name(dub)}.")
    elif result == 0: ##lose
        dub -= bet
        print(f"Oh man! You lost {dub_name(bet)}, so now you have {dub_name(dub)}.")
    else: ##tie
        print("Since you tied, nothing changes with your Doubloons")

    will = False

    time.sleep(1.5) 
    if dub == 0: 
        print("GAME OVER! You're poor as a rat now!\npew pew get shot and die ᡕᠵデᡁ᠊╾━-----💥") 
    else:
        while True:
            will = input("Wanna keep going?(Yes(1) / No(2))\n")
            if will in ['y', 'Y', 'yes', 'Yes', 'yis', '1']:
                will = True
                break
            elif will in ['n','N','No','no','quit', '2']:
                print(f"You finished with {dub_name(dub)}! I'm not smart enough to know if that's good or bad :)")
                break
            else:
                print('Please pick 1 (yes) or 2 (no)')
