from time import sleep
from try_input import tryInput
from dice_display import diceDisplay
from winner_name import winnerNameGenerator
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def mainLoop(diceDict):

    again = 'o'
    while again.upper() != 'N' and again.upper() != 'NON':

        numberOfPerson, face, throwDice = tryInput()
        listOfName = []
        points = []

        for i in range(numberOfPerson):
            name = input(f'Quel est le nom de la personne n°{i+1} \n')
            print('\n')

            listOfName.append(name)
            points.append({'name': name, 'point': 0})

        print('\n\n\n')
        points = diceDisplay(listOfName, throwDice, face, diceDict, points)

        winnerName, highestScore = winnerNameGenerator(points)

        print(f"Le plus haut score est : {Fore.RED}{highestScore}")

        if len(winnerName) > 1:
            print(f"Il y a égalité entre {Fore.GREEN}{', '.join(winnerName)}.")

        else:
            sleep(1)
            print('\n\n\n')
            print("Le gagnant est : ", end="")
            for dot in '..':
                sleep(0.7)
                print(dot, end="", flush=True)
            sleep(0.7)
            print(f'. \n{str(winnerName[0])}')
            print('\n\n\n')
            sleep(3)

        print('Tu veux recommencer ? ')
        print('o - OUI')
        print('n - NON')
        again = input('')

        while(again.upper() != 'O' and again.upper() != 'OUI' and again.upper() != 'N' and again.upper() != 'NON'):
            print("Je n'ai pas compris ! ")
            print('Tu veux recommencer ? ')
            print('o - OUI')
            print('n - NON')
            again = input('')
