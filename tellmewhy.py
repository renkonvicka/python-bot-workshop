#this is the backstreet boy feature i'd like to add to augurybot
looping = True

while looping == True:

    its = input()

    its = its.upper()

    if its == "TELL ME WHY":
        print("Ain't nothin but a heeeart aaache")
        gonna = input()
        gonna = gonna.upper()

    else:
        print("ask me to tell you why. just do it.")
        gonna = input()
        looping = True

        if gonna == "TELL ME WHY":
            print("Ain't nothin but a mistaaaake")
            be = input()
            be = be.upper()

            if be == "TELL ME WHY":
                print("I only wanna hear you sayyyy")
                print("I want it thaaaat wayyyyy")
                looping = False
#may

#FIXNOTE second time typing random input does not get ask me prompt- reverts back to blank output. next random input does recieve ask me prompt.

#==== ask me prompt fix attempt. er: invalid syntax =======
    #else:
        #print("ask me to tell you why. just do it.")
        #looping = True
