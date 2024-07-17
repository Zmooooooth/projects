import csv

def main():
    add_names()
    namedict = read_file()

    for person in sorted(namedict, key=lambda student: student["name"], reverse=True):
        print(f"Hello, {person['name']}. You were born in {person['year_of_birth']}.")

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
            with open("names3.csv","a") as file:
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
    with open("names3.csv","r") as file:
        reader = csv.reader(file)
        for line in reader:
            emptydict = {
                "name": line[0],
                "year_of_birth": line[1]
            }
            #emptydict["name"] = name
            #emptydict["year_of_birth"] = year
            emptylistofdict.append(emptydict)
            emptydict = {}
    return emptylistofdict

if __name__ == "__main__":
    main()
