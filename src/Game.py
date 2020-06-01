from abc import ABC, abstractmethod


class Game(ABC):
    """
An abstract game class:
Attributes
    -------
    difficulty : int
        a number between one to five
Methods
    -------
    play()
        start a new game

        Returns:
            bool True in win case, False otherwise.

    get_user_input() -> object
        Handel user input

    __str__() : string
        get game description
    """
    def __init__(self, difficulty):
        self.difficulty = difficulty
        super().__init__()

    def __str__(self):
        pass

    @abstractmethod
    def get_user_input(self):
        pass

    @abstractmethod
    def play(self):
        pass
