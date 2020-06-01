import random
from time import sleep
from Game import Game
from utils import get_choise, clear


class MemoryGame(Game):
    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.randomList = self._generate_sequence()

    def __str__(self):
        return self.get_description()

    @staticmethod
    def get_description():
        return "Memory Game - a sequence of numbers will appear for 1"
        + "second and you have to guess it back"

    def _generate_sequence(self):
        return [random.randint(1, 101) for i in range(self.difficulty)]

    def get_user_input(self):
        return [
            get_choise(1, 101, "enter {num} num: ".format(num=i+1))
            for i in range(self.difficulty)
        ]

    def _is_list_equal(self, userList):
        equal = True
        for i in range(self.difficulty):
            if self.randomList[i] != userList[i]:
                equal = False
                break
        return equal

    def play(self):
        clear()
        print("Pay attention!, those are the numbers to remember:")
        for num in self.randomList:
            print(num)
        sleep(0.7)
        clear()
        print("enter the numbers that you just saw")
        userList = self.get_user_input()
        return self._is_list_equal(userList)
