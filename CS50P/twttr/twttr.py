def main():
    stringinput = input("Input: ").strip()
    replacementchars = ["A","E","I","O","U","a","e","i","o","u"]
    stringoutput = modifystring(stringinput,replacementchars)
    print(f"Output: {stringoutput}")

def modifystring(input,list):
    for character in list:
        input = input.replace(character,"")
    return input

main()
