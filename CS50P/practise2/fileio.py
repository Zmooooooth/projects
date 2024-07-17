def main():
    add_names()
    namelist = read_file()
    #namelist = namelist.sort()
    for name in sorted(namelist, reverse=True):
        print(f"Hello, {name}")
    print("")
def add_names():
    while True:
        try:
            userin = input("Please enter a Name: ")
            with open("names.txt","a") as file:
                file.write(f"{userin}\n")
        except:
            print("\n")
            break
def read_file():
    emptylist = []
    with open("names.txt","r") as file:
        for line in file:
            emptylist.append(line.rstrip())
    return emptylist

if __name__ == "__main__":
    main()
