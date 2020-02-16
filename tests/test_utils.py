import pytest
import mock
import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

import utils
import io


class TestUtils:
    def test_get_choice(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO('2'))
        # with pytest.raises(ValueError):
        assert utils.get_choise() == 2
