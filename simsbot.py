#a blind recreation of the beloved cheat

open = input()
open = open.upper()

if open == "BOOLPROPTESTINGCHEATSENABLEDTRUE":

    looping = True

    cash = input()
    cash = cash.lower()
    x = 0
    y = 1
    money = 0

    while looping == True:

        if cash == "motherlode":
            y = y + 1
            money = money + 10000
            print(money)
            cash = input()
            looping = True

        elif cash == "exit":
            looping = False

        else:
            print("error: command invalid")
            cash = input()
            looping = True
