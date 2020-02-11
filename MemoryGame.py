import random
from time import sleep
from utils import get_choise, clear


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.randomList = self._generate_sequence()

    def _generate_sequence(self):
        return [random.randint(1, 101) for i in range(self.difficulty)]

    def _get_list_from_user(self):
        return [get_choise(1, 101) for i in range(self.difficulty)]

    def _is_list_equal(self, userList):
        equal = True
        for i in range(self.difficulty):
            if self.randomList[i] != userList[i]:
                equal = False
                break
        return equal

    @staticmethod
    def get_description():
        return "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"

    def play(self):
        clear()
        print("numbers to remember:")
        for num in self.randomList:
            print(num)
        sleep(0.7)
        clear()
        print("enter the numbers that you just saw")
        userList = self._get_list_from_user()
        return self._is_list_equal(userList)
