from random import randint
from time import sleep
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def diceDisplay(listOfName, throwDice, face, diceDict, points):
    for i in range(len(listOfName)):
        total = 0
        dice = [[]]
        numberOfNumber = 0

        for j in range(throwDice):
            firstDice = randint(1, face)
            total += firstDice
            firstDice = '0' + \
                str(firstDice) if len(str(firstDice)) == 1 else firstDice
            index = 0
            numberOfNumber = 0

            for word in str(firstDice):
                for line in diceDict[int(word)]:
                    line = '\u0020\u0020\u0020' + line
                    if numberOfNumber > 0:
                        dice[j][index] = dice[j][index] + line
                        index += 1
                    else:
                        dice[j].append(line)
                numberOfNumber += 1
                index = 0
            dice.append([])

        print(f'{listOfName[i]} a obtenu un : ')
        for number in range(len(dice)):
            for line in dice[number]:
                print(Fore.LIGHTYELLOW_EX + line)
                sleep(0.05)
            sleep(0.5)
            print('\n')

        points[i]['point'] = total

    return points
