import fuel
import pytest

def main():
    test_highnr()

def test_convert():
    assert fuel.convert("1/2") == 50

def test_highnr():
    with pytest.raises(ValueError):
        assert fuel.convert("cat/3")
def test_zerodiv():
    with pytest.raises(ZeroDivisionError):
        assert fuel.convert("12/0")

def test_gauge():
    assert fuel.gauge(20) == "20%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"

if __name__ == "__main__":
    main()
