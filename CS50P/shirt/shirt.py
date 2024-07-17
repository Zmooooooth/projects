import sys
from PIL import Image, ImageOps

def main():
    check_path()
    work_with_input(str(sys.argv[1]))
    pass

def work_with_input(inputpic):
    try:
        shirt = Image.open("shirt.png")
        shirtfile_size = shirt.size
        bp = Image.open(sys.argv[1])
        basepic = ImageOps.fit(bp, size=shirtfile_size)
        basepic.paste(shirt, shirt)
        basepic.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")

def check_path():
    valid_types = [".png",".jpeg",".jpg"]
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if str(sys.argv[1][-4:]).lower() not in valid_types:
        sys.exit("Invalid output")
    if str(sys.argv[2][-4:]).lower() != str(sys.argv[1][-4:]).lower():
        sys.exit("Input and output have different extensions")
    try:
        with open(sys.argv[1], "r") as read:
            pass
    except:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
