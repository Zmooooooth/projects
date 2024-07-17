def main():
    add_names()
    namedict = read_file()
    for person in sorted(namedict, key=get_yob, reverse=True):
        print(f"Hello, {person['name']}. You were born in {person['year_of_birth']}.")
    #for person in namedict:
        #print(f"Hello, {person['name']}. You were born in {person['year_of_birth']}.")
    print("")

def get_name(student):
    return student["name"]

def get_yob(student):
    return student["year_of_birth"]

def add_names():
    while True:
        try:
            userin_name = input("Please enter a Name: ")
            user_year_of_birth = get_int()
            with open("names2.csv","a") as file:
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
    emptylistofdict = []
    emptydict = {}
    with open("names2.csv","r") as file:
        for line in file:
            line = line.rstrip()
            name, year = line.split(",")
            emptydict = {
                "name": name,
                "year_of_birth": year
            }
            #emptydict["name"] = name
            #emptydict["year_of_birth"] = year
            emptylistofdict.append(emptydict)
            emptydict = {}
    return emptylistofdict

if __name__ == "__main__":
    main()
