import numb3rs

def test_valid():
    assert numb3rs.validate("127.0.0.1") == True
    assert numb3rs.validate("0.0.0.0") == True
    assert numb3rs.validate("255.255.255.255") == True

def test_to_high():
    assert numb3rs.validate("12.213.2.600") == False
    assert numb3rs.validate("999.999.9999.20") == False
    assert numb3rs.validate("-10.-20.-20.-90") == False

def test_invalid():
    assert numb3rs.validate("Hello world!") == False
    assert numb3rs.validate("213.213214.235.345.6254.6524.6254.254.625.62.54.235") == False
