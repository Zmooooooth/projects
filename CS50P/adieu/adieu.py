

def main():

    userinput = input_names()
    out = process_string(userinput)
    print(out)

def input_names():
    namelist = []
    while True:
        try:
            inputusr = input("Name: ")
        except:
            print("")
            return namelist
        else:
            namelist.append(inputusr)

def process_string(inputlist):
    namestring = "Adieu, adieu, to "
    if len(inputlist) == 1:
        resultstring = namestring + inputlist[0]
        return resultstring
    if len(inputlist) == 2:
        resultstring = namestring + inputlist[0] + " and " + inputlist[1]
        return resultstring
    if len(inputlist) > 2:
        stringempty = ""
        for name in inputlist[:-2]:
            stringempty = stringempty + f"{name}, "
        namestring = namestring + stringempty + inputlist[-2] + ", and " + inputlist[-1]
        return namestring

if __name__ == "__main__":
    main()
