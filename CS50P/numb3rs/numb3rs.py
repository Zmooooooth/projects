import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        for i in range(4):
            if int(matches.group(i+1)) > 255:
                return False
            else:
                pass
        return True
    else:
        return False




if __name__ == "__main__":
    main()
