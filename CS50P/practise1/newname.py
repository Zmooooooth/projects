import sys

def main():
    try:
        print("Hello! my name is", sys.argv[1])
    except:
        print("please enter:python newname.py [YourName]")
        pass
main()
