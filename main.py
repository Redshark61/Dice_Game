#coding: utf-8

from random import randint
from main_loop import mainLoop
import json


def main():
    with open('dice.json', 'r') as f:
        diceDict = json.load(f)

    mainLoop(diceDict)


if __name__ == '__main__':
    main()
