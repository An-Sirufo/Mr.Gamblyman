##Game 1: Predictive Average

def prediction_encryption(to_encrypt):
    creeped = (((to_encrypt + 10) / 2 * 8) - 3 )* 5
    return int(creeped)

print("Welcome to the Predictive Average Game!)
print("\nNow I'll make my prediction...\nI'll encrypt it with this secret formula: +10 /2 *8 -3 *5 so you don't know it")
pred_avg = 5
creeped = prediction_encryption(pred_avg)
print("Your encrypted average is: ", creeped)

while True:
    num1 = input("\nOk, pick a number from 1 to 10: ")
    if not num1.isdigit():
        print("Needs to be a number!")
    else:
        break

while True:        
    num2 = input("Another one please: ")
    if not num2.isdigit():
        print("Needs to be a number!")
    else:
        break

real_avg = (int(num1) + int(num2)) / 2
print("Your real average is: ", int(real_avg))
print("Let's desencrypt my prediction and see if I was right...")
print(creeped, "/5 =", creeped / 5, "\n+3 is", (creeped / 5) + 3, "\n/8 is", ((creeped / 5) + 3) / 8, "\n*2 is", (((creeped / 5) + 3) / 8) * 2, "\n-10 is", ((((creeped / 5) + 3) / 8) * 2) - 10)

if real_avg == pred_avg:
    print("\nSee, I was right, I predicted", float(pred_avg), "and your average is", real_avg)
else:
    print("\nSucks to suck, I got it wrong, I predicted", float(pred_avg), "and your average is", real_avg)
## for the future, add a class to set parameters for the user, so I can make more accurate predictions
