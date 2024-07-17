import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not check_banned_chars(s):
        return False
    if len(s) < 2 or len(s) > 6:
        #print("has wrong length")
        return False
    #print("has right length")
    if not check_two_letters(s):
        return False
    if check_zero_start(s):
        return False
    if check_last_if_letter(s):
        return False
    if check_if_number_in_middle(s):
        return False
    else:
        return True
def check_last_if_letter(input):
    srch = False
    list_of_numbers = ["0","1","2","3","4","5","6","7","8","9"]
    for number in list_of_numbers:
        if number in input:
            srch = True
    if srch:
        uppercase_letters = list(string.ascii_uppercase)
        for char in uppercase_letters:
            if input[-1] == char:
                return True
        return False
def check_if_number_in_middle(input):
    index = 0
    list_of_numbers = ["0","1","2","3","4","5","6","7","8","9"]
    uppercase_letters = list(string.ascii_uppercase)
    try:
        for character in input:
            for number in list_of_numbers:
                if character == number:
                    for letter in uppercase_letters:
                        if letter == input[index + 1]:
                            return True
            index = index + 1
        return False
    except:
        return False


def check_two_letters(input):
    counter = 0
    uppercase_letters = list(string.ascii_uppercase)
    for char in uppercase_letters:
        if char == input[0]:
            counter += 1
        if char == input[1]:
            counter += 1
    if counter == 2:
        #print("Has two letters in beginning")
        return True
    else:
        #print("does not have two letters in the beginning")
        return False
def check_zero_start(input):
    uppercase_letters = list(string.ascii_uppercase)
    for letter in uppercase_letters:
        input = input.replace(letter,"")
    try:
        if input[0] == "0":
            #print("First number is 0")
            return True
        else:
            #print("0 is not the first number")
            return False
    except:
        return False

def check_banned_chars(input):
    banned_chars = [" ",".",",",":",";"]
    for character in banned_chars:
        if character in input:
            return False
    #print("no banned characters")
    return True

if __name__ == "__main__":
    main()
