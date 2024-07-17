import sys

def main():

    path = check_path()
    all_lines = scan_file(path)
    complexity_counter = 0
    for line in all_lines:
            if line == "\n" or line.strip().startswith("#") == True or len(line.strip()) < 1:
                continue
            else:
                complexity_counter += 1
    print(complexity_counter)

def scan_file(filepath):
    try:
        with open(filepath, "r") as file:
            all_lines = file.readlines()
        return all_lines
    except:
        sys.exit("File does not exist")

def check_path():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not ".py" in sys.argv[1]:
        sys.exit("Not a Python file")
    else:
        return sys.argv[1]

if __name__ == "__main__":
    main()
