#the beloved augury charm, turned into a magic 8 ball

print("What knowledge does your heart desire?")

import random

input()

randomNumber = random.randint(0, 101)

if randomNumber <= 10:
    print ("Reply inappropriate, try again.")

elif randomNumber <= 20:
    # and randomNumber >= 11
    print("I don't respond to commoners.")

elif randomNumber <= 30:
    print("Looks like it to me.")

elif randomNumber <= 40:
    print("Not a snowball's chance in hell.")

elif randomNumber <= 50:
    print("Good luck, champ.")

elif randomNumber <= 60:
    print("No.")

elif randomNumber <= 70:
    print("-distant laughter-")

elif randomNumber <= 80:
    print("Why would you even ask that?")

elif randomNumber <= 90:
    print("I asked the void and the void screamed, I'm taking that as a maybe.")

else:
    print("Honestly at this point why not?")

    #===== backstreet boy feature to be added ==========
