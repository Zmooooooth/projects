import sys

def main():
    userin = input("Input: ")
    string = gauge(convert(userin))
    print(string)

def convert(fraction):
    fraction = fraction.replace(" ","")
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    result = x / y
    result = result * 100
    if x > y:
        sys.exit("ValueError")
    return int(result)



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
