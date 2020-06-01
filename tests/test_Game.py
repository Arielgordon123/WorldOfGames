from Game import Game
import pytest
import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))


class TestGame:
    def test_abstract(self):
        with pytest.raises(TypeError):
            Game()
