from os import system, name


def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')


def get_choise(min=1, max=3, message="Please enter your choise: "):
    try:
        choise = int(input(message))
        if choise > max or choise < min:
            raise ValueError
        return choise
    except ValueError:
        print("not a valid choise, please try again")
        return get_choise(min, max)
