def main():
    #printcolumn(50,6)
    printsquare(5)

def printcolumn(distance,height):
    emptystring = ""
    for _ in range(distance):
        emptystring = emptystring + " "
    for i in range(height):
        if i == height - 1:
            print(emptystring.replace(" ", "_") + "#", sep="")
        else:
            print(emptystring + "#", sep="", end="\n")

def printsquare(height):
    for i in range(height):
        for _ in range(height):
            print("#", end="")
        print("\n", end="")


main()
