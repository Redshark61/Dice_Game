import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def tryInput():
    while True:
        try:
            numberOfPerson = int(input('Combien il y a de personnes\n'))
            print('\n')
            break
        except:
            print(Fore.RED+"Veuillez rentrer un nombre")
    while True:
        try:
            face = int(input('Combien il y a de face au dé\n'))
            print('\n')

            break
        except:
            print(Fore.RED+"Veuillez rentrer un nombre")
    while True:
        try:
            throwDice = int(input('Combien il y a de lancer\n'))
            print('\n')
            break
        except:
            print(Fore.RED+"Veuillez rentrer un nombre")

    return numberOfPerson, face, throwDice
