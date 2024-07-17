def main():

    x = get_int()
    print(f"This is your number: {x}")


def get_int():
    while True:
        try:
            number = int(input("Please enter a number: "))
        except ValueError:
            #print("This is not an integer!")
            pass
        else:
            break
    return number

main()
