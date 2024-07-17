import emoji
def main():

    userinput = input("Input: ")
    try:
        string = emoji.emojize(userinput,language="alias")
        print(string)
    except:
        pass


if __name__ == "__main__":
    main()
