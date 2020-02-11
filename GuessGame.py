import random
from utils import get_choise


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self._generate_number(self)

    def _generate_number(self):
        self.secret = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        return get_choise(min=1, max=self.difficulty+1)

    def compare_results(self, guess):
        return guess == self.secret

    def play(self):
        guess = self.get_guess_from_user()
        return self.compare_results(guess)
