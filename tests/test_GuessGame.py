from GuessGame import GuessGame
import pytest  # noqa: F401
import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))


class TestGuessGame:
    def test_description(self):
        assert GuessGame.get_description().startswith("Guess Game")

    def test_guess(self):
        guessGame = GuessGame(1)
        assert guessGame.compare_results(1)

    def test_generate(self):
        game = GuessGame(3)
        assert isinstance(game.secret, int)
