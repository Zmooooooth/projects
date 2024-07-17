import pytest
from unittest.mock import patch
import project

def test_await_userinput():
    with patch('builtins.input', return_value='e'):
        assert project.await_userinput() == 'e'

def test_show_startpage():
    with pytest.raises(IndexError):
        assert project.show_startpage([]) == []

def test_get_valid_float():
    with patch('builtins.input', return_value=1.0):
        assert project.get_valid_float("1.0")

def test_show_portfolio():
    emptydic = []
    assert project.show_portfolio(emptydic) == True
