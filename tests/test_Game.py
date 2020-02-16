import pytest
import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from Game import Game


class TestGame:
    def test_abstract(self):
        with pytest.raises(TypeError):
            Game()
