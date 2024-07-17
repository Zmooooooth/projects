def main():

    userin = input("Greeting: ")
    out = value(userin)
    print(f"${out}")


def value(greeting):
    greeting = greeting.lower()
    number = 100
    if("hello" in greeting):
        number = 0
    elif(greeting.startswith("h")):
        number = 20
    else:
        pass
    return int(number)


if __name__ == "__main__":
    main()
