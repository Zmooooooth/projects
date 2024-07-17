def main():
    dict = get_input()
    sorted_keys = sorted(dict.keys())
    sorted_dict = {key: dict[key] for key in sorted_keys}
    for item in sorted_dict:
        print(f"{sorted_dict[item]} {item}")
#comment






def get_input():
    grocerylist = {}
    while True:
        try:
            userinput = input("").strip().upper()
            if userinput in grocerylist:
                grocerylist[userinput] = grocerylist[userinput] + 1
            else:
                grocerylist[userinput] = 1
        except:
            print("")
            return grocerylist
main()
