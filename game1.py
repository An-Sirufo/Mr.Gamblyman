##Game 1: Predictive Average

import time


def prediction_encryption(to_encrypt):
    creeped = (((to_encrypt + 10) / 2 * 8) - 3 )* 5
    return int(creeped)

print("Welcome to the Predictive Average Game!")
time.sleep(1)
print("Now I'll make my prediction...")
time.sleep(1)
print("I'll encrypt it with this secret formula: +10 /2 *8 -3 *5 so you don't know it")
pred_avg = 5
creeped = prediction_encryption(pred_avg)
time.sleep(2)
print("Your encrypted average is:", creeped)
time.sleep(1)

while True:
    num1 = input("\nOk, pick a number from 1 to 10: ")
    if not num1.isdigit():
        print("Needs to be a number!")
    else:
        break
time.sleep(0.5)

while True:        
    num2 = input("Another one please: ")
    if not num2.isdigit():
        print("Needs to be a number!")
    else:
        break

real_avg = (int(num1) + int(num2)) / 2
time.sleep(1)
print("Your real average is: ", int(real_avg))
time.sleep(1)
print("Let's desencrypt my prediction and see if I was right...")
time.sleep(2)
print(creeped, "/5 is", creeped / 5)
time.sleep(1)
print("+3 is", (creeped / 5) + 3)
time.sleep(1)
print("/8 is", ((creeped / 5) + 3) / 8)
time.sleep(1)
print("*2 is", (((creeped / 5) + 3) / 8) * 2)
time.sleep(1)
print("-10 is", ((((creeped / 5) + 3) / 8) * 2) - 10)
time.sleep(2)

print("\nSo my prediction was", float(pred_avg))
time.sleep(1)

if real_avg == pred_avg:
    print("\nSee, I was right, I predicted", float(pred_avg), "and your average is", real_avg)
else:
    print("\nSucks to suck, I got it wrong, I predicted", float(pred_avg), "and your average is", real_avg)
## for the future, add a class to set parameters for the user, so I can make more accurate predictions
