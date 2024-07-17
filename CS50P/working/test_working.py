import working
import pytest

def test_time():
    assert working.convert("7 AM to 8 PM") == "07:00 to 20:00"
    assert working.convert("8 PM to 7 AM") == "20:00 to 07:00"

def test_2():
    assert working.convert("11:21 AM to 03:23 PM") == "11:21 to 15:23"

def test_3():
    with pytest.raises(ValueError):
        assert working.convert("abscedf")
        assert working.convert("11:21 AM to 03:23 PM 11:21 AM to 03:23 PM")
        assert working.convert("125:21 AM to 13:23 PM")

def test_4():
    with pytest.raises(ValueError):
        assert working.convert("11:60 AM to 10:23 PM")
def test_5():
    with pytest.raises(ValueError):
        assert working.convert("9:60 AM to 5:60 PM")
def test_6():
    with pytest.raises(ValueError):
        assert working.convert("9 AM - 5 PM")

def test_7():
    with pytest.raises(ValueError):
        assert working.convert("09:00 AM to 17:00 PM")

def test_8():
    with pytest.raises(ValueError):
        assert working.convert(":10 AM to :200 PM")

