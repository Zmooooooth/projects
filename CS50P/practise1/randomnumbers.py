import random


def main():
    headcount = 0
    tailcount = 0
    #mylist = ["Apple","Beer","Banana","Juice"]
    #result = random.choice(mylist)
    #print(f"You need: {result}")
    coinstate = ["Heads","Tails"]
    for _ in range(getuser_int()):
        result = random.choice(coinstate)
        if result == "Heads":
            headcount += 1
        else:
            tailcount +=1
    sum = headcount + tailcount
    headcount = headcount / sum
    tailcount = tailcount / sum
    headcount = headcount * 100
    tailcount = tailcount * 100
    print(f"{sum} coins flipped. Heads: {headcount:.2f}%, Tails: {tailcount:.2f}%")

def getuser_int():
    while True:
        try:
            inp = int(input("How many flips? "))
        except ValueError:
            print("Not a valid Integer!")
            pass
        else:
            if inp > 0:
                return inp
            else:
                print("Not a valid Integer!")
                continue

main()
