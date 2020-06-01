from CurrencyRouletteGame import CurrencyRouletteGame
import pytest  # noqa: F401
import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))


class TestCurrencyRouletteGame:
    def test_api(self):
        game = CurrencyRouletteGame(1)
        assert CurrencyRouletteGame._api_url.startswith("http")
        min_intervel = game.interval['min']
        assert isinstance(min_intervel, float)

    def test_description(self):
        assert CurrencyRouletteGame.get_description().startswith(
            "Currency Roulette")

    def test_compare_results(self):
        game = CurrencyRouletteGame(1)
        game.interval = {"min": 100.0, "max": 102.3}
        assert game._compare_results(100)
        assert not game._compare_results(99.9)
        assert not game._compare_results(102.31)
