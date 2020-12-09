import random
from colorama import init
init()
from coloramaimport Fore, Back, Style

listeMot = [ "clamer" , "inhale" , "eclair" , "tourne" , "voiler" , "fourmi", "comble", "inclus" , "chante" , "retard" ]
Mot = random.choice(listeMot)
print (Mot)