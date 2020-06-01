import random
from Game import Game
from utils import get_choise


class GuessGame(Game):
    def __init__(self, difficulty):
        super().__init__(difficulty)
        self._generate_number()

    def __str__(self):
        return self.get_description()

    @staticmethod
    def get_description():
        return "Guess Game - guess a number and see if you choosed like the computer"

    def _generate_number(self):
        self.secret = random.randint(1, self.difficulty)

    def get_user_input(self):
        return get_choise(min=1, max=self.difficulty, message="I picked a number, can you guess it? ")

    def compare_results(self, guess):
        return guess == self.secret

    def play(self):
        guess = self.get_user_input()
        return self.compare_results(guess)
