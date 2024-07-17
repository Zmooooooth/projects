from twttr import shorten

def main():
    test_string()
    test_numbr()

def test_string():
    assert shorten("String") == "Strng"
    assert shorten("str1ng") == "str1ng"
    assert shorten("UPPERCASE") == "PPRCS"

def test_numbr():
    assert shorten("12345") == "12345"
    assert shorten("12367") == "12367"

def test_punctuation():
    assert shorten(".:$%") == ".:$%"

if __name__ == "__main__":
    main()
