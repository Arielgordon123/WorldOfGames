from utils import get_choise

def welcome(name):
    return "Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.".format(name=name)


def load_game():
    game_options = ["1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
                    "2. Guess Game - guess a number and see if you chose like the computer",
                    "3. Currency Roulette - try and guess the value of a random amount of USD in ILS"]
    for game in game_options:
        print(game)
    choise = get_choise(1, len(game_options))
    print("Please choose game difficulty from 1 to 5:")
    difficulty = get_choise(1, 5)
