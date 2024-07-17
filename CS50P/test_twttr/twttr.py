def main():
    usrin = input("Input: ")
    out = shorten(usrin)
    print(out)

def shorten(word):
    vowel_list = ["A","E","I","O","U","a","e","i","o","u"]
    for vowel in vowel_list:
        if vowel in word:
            word = word.replace(vowel, "")
    return word


if __name__ == "__main__":
    main()
