from bank import value
def main():
    test_numberinput()
    test_str_without_h()
    test_str_spec_chars()

def test_numberinput():
    assert value("1234") == 100
    assert value ("0") == 100
def test_str_without_h():
    assert value("What's up") == 100
    assert value("hey") == 20
    assert value("Hello") == 0
    assert value("hello") == 0
def test_str_spec_chars():
    assert value(".!,") == 100
    assert value("?!?") == 100

if __name__ == "__main__":
    main()
