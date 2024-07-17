def main():
    height = get_int()
    create_pyramid(height)

def get_int():
    while True:
        usernumber = input("Height: ")
        try:
            if int(usernumber) > 0 and int(usernumber) < 9:
                return int(usernumber)
        except ValueError:
            continue

def create_pyramid(height):
    for x in range(height):
        a = height
        while a > x + 1:
            print(" ",end="")
            a -= 1
        b = 1
        while b <= x + 1:
            print("#",end="")
            b += 1
        print("  ",end="")
        c = 1
        while c <= x + 1:
            print("#",end="")
            c += 1
        print("\n",end="")

if __name__ == "__main__":
    main()
