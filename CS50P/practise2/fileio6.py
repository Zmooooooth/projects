import csv

name = input("What's your name? ")
year = input("What year were you born? ")

#with open("names4.csv", "a") as file:
    #writer = csv.writer(file)
    #writer.writerow([name,year])

with open("names4.csv", "a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","year_of_birth"])
    dictionary = {
        "name": name,
        "year_of_birth": year
    }
    writer.writerow(dictionary)
