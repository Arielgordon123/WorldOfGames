

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


def get_choise(min=1, max=3):
    try:
        choise = int(input("Please enter your choise: "))
        if choise > max or choise < min:
            raise ValueError
        return choise
    except ValueError:
        print("not a valid choise, please try again")
        return get_choise(min, max)
