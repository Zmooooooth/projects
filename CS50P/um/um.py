import re
import sys


def main():
    print(count(input("Text: "))).strip()


def count(s):
    counter = 0
    counter = counter + len(re.findall(r"\b(um)\b[.,!?]*\s*",s,re.IGNORECASE))
    return counter


...


if __name__ == "__main__":
    main()
