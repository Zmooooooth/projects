def main():
    add_names()
    namedict = read_file()
    #namelist = namelist.sort()
    for name in sorted(namedict, reverse=True):
        print(f"Hello, {name}. You are born in {namedict[name]}")
    print("")
def add_names():
    while True:
        try:
            userin_name = input("Please enter a Name: ")
            user_year_of_birth = get_int()
            with open("names.csv","a") as file:
                file.write(f"{userin_name},{user_year_of_birth}\n")
        except:
            print("\n")
            break
def get_int():
    while True:
        try:
            userin = int(input("Enter year of birth: "))
        except:
            print("Not a valid year")
        else:
            if 0 < userin < 3000:
                return userin
            else:
                pass

def read_file():
    emptydict = {}
    with open("names.csv","r") as file:
        for line in file:
            line = line.rstrip()
            name, year = line.split(",")
            emptydict[name] = year
    return emptydict

if __name__ == "__main__":
    main()
