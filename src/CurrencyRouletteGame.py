import requests
import random
from Game import Game
from utils import get_choise, clear


class CurrencyRouletteGame(Game):

    _api_url = "https://api.exchangeratesapi.io/latest?symbols=ILS&base=USD"

    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.interval = self._get_money_interval()

    def __str__(self):
        return self.get_description()

    @staticmethod
    def get_description():
        return "Currency Roulette - try and guess the value of a random amount of USD in ILS"

    def _get_money_interval(self):
        total = random.randint(1, 100)
        response = requests.get(self._api_url).json()
        ils_usd_rate = response['rates']['ILS']
        return {"min": ils_usd_rate * (total - (5 - self.difficulty)),
                "max": ils_usd_rate * (total + (5 - self.difficulty))}

    def get_user_input(self):
        message = "could you geuss the value of x USD in ILS? "
        return get_choise(min=1, max=1000, message=message, type=float)

    def _compare_results(self, guess):
        if guess >= self.interval['min'] and guess <= self.interval['max']:
            return True
        return False

    def play(self):
        clear()
        user_guess = self.get_user_input()
        return self._compare_results(user_guess)
