from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRouletteGame
from MemoryGame import MemoryGame
from utils import get_choise


def welcome(name):
    return "Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.".format(name=name)


def load_game():
    games = [MemoryGame, GuessGame, CurrencyRouletteGame]
    for i, game in enumerate(games):
        print("{num}: {description}".format(
            num=i+1, description=game.get_description()))
    choise = get_choise(1, len(games))
    difficulty = get_choise(
        min=1, max=5, message="Please choose game difficulty from 1 to 5: ")
    result = games[choise-1](difficulty).play()
    if result:
        print("you Won!")
    else:
        print("you lose, try again")


load_game()
