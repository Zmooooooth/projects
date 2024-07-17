import math

def main():
    userin = get_userinput()
    response = checksum(userin)
    if response:
        if ((userin >= 340000000000000 and userin < 350000000000000) or (userin >= 370000000000000 and userin < 380000000000000)):
                print("AMEX")
        elif (userin >= 5100000000000000 and userin < 5600000000000000):
            print("MASTERCARD")
        elif ((userin >= 4000000000000 and userin < 5000000000000) or (userin >= 4000000000000000 and userin < 5000000000000000)):
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")

def checksum(number):
    result1 = 0
    result2 = 0

    first = True

    while number != 0:
        if first:
            result1 = result1 + number % 10
            number = math.floor(number / 10)
            first = False
        else:
            next_num = (number % 10) * 2
            if next_num > 9:
                result2 = result2 + next_num % 10 + math.floor(next_num / 10)
            else:
                result2 = result2 + next_num
            number = math.floor(number / 10)
            first = True

    result = result1 + result2
    if result % 10 == 0:
        return True
    else:
        return False

def get_userinput():
    while True:
        userin = input("Number: ")
        try:
            userin = int(userin)
            if userin > 0:
                return userin
        except ValueError:
            continue

if __name__ == "__main__":
    main()
