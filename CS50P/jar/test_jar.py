import jar
import pytest

def test_1():
    my_jar = jar.Jar()
    my_jar.deposit(2)
    assert my_jar.__str__() == "🍪🍪"

def test_2():
    my_jar = jar.Jar()
    my_jar.deposit(2)
    my_jar.withdraw(1)
    assert my_jar.__str__() == "🍪"

def test_3():
    my_jar = jar.Jar()
    my_jar.deposit(2)
    with pytest.raises(ValueError):
        my_jar.withdraw(10)

def test_4():
    my_jar = jar.Jar()
    with pytest.raises(ValueError):
        my_jar.deposit(20)
