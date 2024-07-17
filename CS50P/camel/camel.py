import re
def main():
    userinput = input("camelCase: ").strip()
    output = convert_to_snake_case(userinput)
    print(f"snake_case: {output}")

def convert_to_snake_case(input):
    modifiedinput = re.sub(r"([A-Z])",r"_\1",input)
    return modifiedinput.lower()
    #TODO

main()
