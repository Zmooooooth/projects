import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^([0-9]+):?([0-5][0-9])? ([AP]M) to ([0-9]+):?([0-5][0-9])? ([AP]M)$"
    if matches := re.match(pattern, s, re.IGNORECASE):
        result = matches.groups()
        if int(result[0]) > 12:
            raise ValueError
        if int(result[3]) > 12:
            raise ValueError
        if filled_list(result):
            pass
        else:
            raise ValueError
        h1, m1 = changeformat(result[0],result[1],result[2])
        h2, m2 = changeformat(result[3],result[4],result[5])
        string = f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"
        return string
    else:
        raise ValueError

def changeformat(hour, minute, type):

    if type == "AM":
        if int(hour) == 12:
            new_h = 0
        else:
            new_h = int(hour)
    if type == "PM":
        if int(hour) == 12:
            new_h = 12
        else:
            new_h = int(hour) + 12
    if minute == None:
        new_m = 0
    else:
        new_m = int(minute)
    return new_h, new_m


def filled_list(result_list):
    try:
        if int(result_list[1]) > 59 or int(result_list[1]) < 0:
            raise ValueError
    except:
        pass
    try:
        if int(result_list[4]) > 59 or int(result_list[4]) < 0:
            raise ValueError
    except:
        pass
    return True


if __name__ == "__main__":
    main()
