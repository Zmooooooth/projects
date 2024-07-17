import sys
import csv
import tabulate

def main():
    check_path()
    return_list = []
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        for line in reader:
            emptylist = [line[0],line[1],line[2]]
            return_list.append(emptylist)

    print(tabulate.tabulate(return_list[1:], return_list[0], tablefmt="grid"))


def check_path():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if str(sys.argv[1][-4:]) != ".csv":
        #print(sys.argv[1][-3:])
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1], "r") as read:
            pass
    except:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
