def getuser_int_positive(question):
    while True:
        try:
            inp = int(input(question))
        except ValueError:
            #print("Not a valid Integer!")
            pass
        else:
            if inp in [1,2,3]:
                return inp
            else:
                #print("Not a valid Integer!")
                continue

if __name__ == "__main__":
    print("This file is not meant to be run directly!")
