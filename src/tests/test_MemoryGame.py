from MemoryGame import MemoryGame
import pytest  # noqa: F401
import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))


class TestMemoryGame:
    def test_description(self):
        assert MemoryGame.get_description().startswith("Memory Game")

    def test_sequence(self):
        memory_game = MemoryGame(5)
        assert len(memory_game._generate_sequence()) == 5

    def test_is_equal(self):
        memory_game = MemoryGame(3)
        memory_game.randomList = [1, 2, 3]
        assert memory_game._is_list_equal([1, 2, 3])
