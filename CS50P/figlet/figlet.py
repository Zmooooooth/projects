import sys
import pyfiglet
import random

def main():
    all_fonts = pyfiglet.FigletFont.getFonts()
    if len(sys.argv) == 0:
        sys.exit("Invalid usage")
    elif len(sys.argv) == 1:
        userinput = input("Input: ")
        random_font = random.choice(all_fonts)
        f = pyfiglet.figlet_format(userinput, font=random_font)
        print(f)
    elif len(sys.argv) == 3 and sys.argv[1] == "-f" or len(sys.argv) == 4 and sys.argv[1] == "--font":
        if sys.argv[2] not in all_fonts:
            sys.exit("Invalid usage")
        else:
            userinput = input("Input: ")
            f = pyfiglet.figlet_format(userinput, font=sys.argv[2])
            print(f)
    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()
