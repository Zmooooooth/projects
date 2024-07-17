import sys
import csv

def main():
    check_path()
    out = read_data(sys.argv[1])
    #print(out)
    write_data(sys.argv[2],out)
    pass

def write_data(target_filename,list_dict):
    with open(target_filename, "w") as file:
        writer = csv.DictWriter(file,fieldnames=["first","last","house"])
        writer.writerow({"first": "first","last": "last","house": "house"})
        for dictionary in list_dict:
            writer.writerow(dictionary)

def read_data(filename):
    dict_list = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            last, first = line["name"].replace(" ","").split(",")
            emptydict = {
                "first": first,
                "last": last,
                "house": line["house"]
            }
            dict_list.append(emptydict)
            emptydict = {}
    return dict_list



def check_path():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if str(sys.argv[1][-4:]) != ".csv":
        sys.exit("Not a CSV file")
    if str(sys.argv[2][-4:]) != ".csv":
        sys.exit("The output file needs to be a csv file")
    try:
        with open(sys.argv[1], "r") as read:
            pass
    except:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()
