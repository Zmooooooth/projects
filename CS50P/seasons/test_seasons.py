import pytest
import seasons

def test_1():
    with pytest.raises(SystemExit):
        assert seasons.process_inp("2007 70 70")

def test_2():
    assert seasons.process_inp("2024-05-28") == "Zero minutes"
