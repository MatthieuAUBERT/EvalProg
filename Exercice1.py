import random
import string
from colorama import init
init()
from colorama import Fore, Back, Style

def compteur(Mot):
    alphabet = list(string.ascii_lowercase)
    compteur = []
    compte = 0
    for i in range (0,len(alphabet)):
        compte = Mot.count(alphabet[i])
        if compte !=0 :
            compteur.append(compte)
    return compteur


listeMot = [ "clamer" , "inhale" , "eclair" , "tourne" , "voiler" , "fourmi", "comble", "inclus" , "chante" , "contre" ]
Mot = random.choice(listeMot)
print (Mot)

for Essais in range (0,8):
    playerInput = input("Saisir votre mot de 6 lettres")
    for i in range (0,6):
        if Mot[i] == playerInput[i]:
            print ( Back.RED + playerInput[i] )
        else:
            color = False
            for j in range (0,6):
                if Mot[i] == playerInput[j]:
                    print ( Back.YELLOW + playerInput[i])
                    color = True
            if color == False :
                print ( Back.BLUE + playerInput[i] )                
    if Mot == playerInput :
        print (Back.RED + playerInput)
        print ("Vous avez gagné")
        exit()
print ("Vous avez perdu")

