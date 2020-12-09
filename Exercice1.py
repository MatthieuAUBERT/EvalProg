import random
from colorama import init
init()
from colorama import Fore, Back, Style

listeMot = [ "clamer" , "inhale" , "eclair" , "tourne" , "voiler" , "fourmi", "comble", "inclus" , "chante" , "contre" ]
Mot = random.choice(listeMot)
print (Mot)


for Essais in range (0,8):
    playerInput = input("Saisir votre mot de 6 lettres")
    for i in range (0,6):
        if Mot[i] == playerInput[i]:
            print ( Back.RED + Mot[i] )
        else:
            color = False
            for j in range (0,6):
                if Mot[i] == playerInput[j]:
                    print ( Back.YELLOW + Mot[i])
                    color = True
            if color == False :
                print ( Back.BLUE + Mot[i] )                
    if Mot == playerInput :
        print ("Vous avez gagné")
        exit()
print ("Vous avez perdu")
