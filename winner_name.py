from time import sleep
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def winnerNameGenerator(points):
    highestScore = 0
    winnerName = []
    for player in points:
        print(
            f"Le nombre de point est: {Fore.CYAN}{player['point']} pour {player['name']}")
        sleep(2)

        if player['point'] > highestScore:

            highestScore = player['point']

            if len(winnerName) == 0:
                # On ajoute juste son nom dans la liste
                winnerName.append(player['name'])

            else:
                winnerName.clear()
                winnerName.append(player['name'])

        elif player['point'] == highestScore:
            winnerName.append(player['name'])

    return winnerName, highestScore
