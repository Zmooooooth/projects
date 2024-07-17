from plates import is_valid

def main():
    test_rightplate()
    test_wrongnumber()
    test_false_char()
    pass

def test_wrongnumber():
    assert is_valid("AA2A") == False
    assert is_valid("0123") == False
    assert is_valid("AA03") == False
def test_rightplate():
    assert is_valid("AA345") == True
    assert is_valid("NMBR") == True
def test_false_char():
    assert is_valid("!_!") == False
def test_length():
    assert is_valid("A") == False
    assert is_valid("asdokjghfdkausfa") == False
def test_beginning():
    assert is_valid("AA123") == True
    assert is_valid("..123AA") == False
def test_start():
    assert is_valid("AA1") == True
    assert is_valid("A1") == False
    assert is_valid("11") == False
def check_numbers():
    assert is_valid("12345") == False
def test_alph_numeric():
    assert is_valid("PI3.14") == False

if __name__ == "__main__":
    main()
