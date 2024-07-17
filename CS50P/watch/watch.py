import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r".*src=\"(https?://(www\.)?youtu)be\.com/embed/([a-zA-Z0-9]+)\".*",s):
            prefix = matches.group(1)
            emmbed = matches.group(3)
            return_string = f"https://youtu.be/{emmbed}"
            return return_string
    else:
        return None


if __name__ == "__main__":
    main()
