import requests


class CurrencyRouletteGame:

    def __init__(self, difficulty):
        self.difficulty = difficulty

    @staticmethod
    def get_description():
        return "Currency Roulette - try and guess the value of a random amount of USD in ILS"

    def get_money_interval(self):
        ils_usd = requests.get("https://api.exchangeratesapi.io/latest?symbols=ILS&base=USD").json()
