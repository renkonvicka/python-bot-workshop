#bot build practice on vacation

print("give me some nachos.")

bro = input()

looping = True

while looping == True:

    if bro.upper() == "SURE":
        print("thanks, man.")
        looping = False

    else:
        print("what?")
        bro = input()
        looping = True
