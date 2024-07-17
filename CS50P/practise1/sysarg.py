import sys
def main():

    if len(sys.argv) < 2:
        sys.exit()
    for arg in sys.argv[1:]:
        print(f"my name is {arg}!")

main()
