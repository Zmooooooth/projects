from datetime import date, datetime
import inflect
import re
import sys

def main():
    userinput = input("Input: ")
    print(process_inp(userinput))

def validate_input(inp):
    try:
        inpt = date.fromisoformat(inp)
        return inpt
    except ValueError:
        sys.exit("Invalid Date")

def process_inp(input):
    input = validate_input(input)
    curr_date = date.today()
    diffrence = curr_date - input
    res_mins = diffrence.days * 24 * 60
    res_mins = int(res_mins)
    rs = inflect.engine().number_to_words(res_mins)
    rs = rs.capitalize()
    rs = rs.replace(" and", "")
    rs = rs + " minutes"
    return rs


if __name__ == "__main__":
    main()
