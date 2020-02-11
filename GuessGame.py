import random
from utils import get_choise


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self._generate_number()

    def _generate_number(self):
        self.secret = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        return get_choise(min=1, max=self.difficulty+1)

    def compare_results(self, guess):
        return guess == self.secret

    @staticmethod
    def get_description():
        return "Guess Game - guess a number and see if you chose like the computer"

    def play(self):
        guess = self.get_guess_from_user()
        return self.compare_results(guess)
