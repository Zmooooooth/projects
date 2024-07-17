def main():

    result = getuserinput()
    if result >= 99 or result == 100:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(f"{result}%")

def getuserinput():
    while True:
        inp = input("Fraction: ")
        try:
            a, b = inp.split("/")
            a = int(a)
            b = int(b)
            result = round(a / b, 2)
        except:
            pass
        else:
            result = result * 100
            if result > 100:
                continue
            else:
                return int(result)

main()
