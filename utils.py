

def get_choise(min=1, max=3):
    try:
        choise = int(input("Please enter your choise: "))
        if choise > max or choise < min:
            raise ValueError
        return choise
    except ValueError:
        print("not a valid choise, please try again")
        return get_choise(min, max)
