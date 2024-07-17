
def main():
    userinput = input("Text: ")
    letters = get_letters(userinput)
    words = get_words(userinput)
    sentences = get_sentences(userinput)
    L = calc_L(words,letters)
    S = calc_S(words,sentences)
    result = calc_formula(L,S)
    if result <= 0:
        print("Before Grade 1")
    elif result > 16:
        print("Grade 16+")
    else:
        print(f"Grade {result}")

def calc_L(words,letters):
    sum = (letters / words) * 100
    return sum

def calc_S(words,sentences):
    result = (sentences / words) * 100
    return result

def calc_formula(L,S):
    result = 0.0588 * L - 0.296 * S - 15.8
    result = round(result)
    return result

def get_letters(text):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters = 0
    for letter in text:
        if str(letter).lower() in alphabet:
            letters += 1
    return letters

def get_words(text):
    words = 1
    for character in text:
        if str(character).lower() == ' ':
            words += 1
    return words

def get_sentences(text):
    sentences = 0
    valid_chars = ['!','?','.']
    for character in text:
        if str(character).lower() in valid_chars:
            sentences += 1
    return sentences

if __name__ == "__main__":
    main()
