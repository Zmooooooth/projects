def main():
    dictionary = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    get_userinput(dictionary)

def get_userinput(dictionary):
    cost = 0
    while True:
        try:
            userinput = input("Item: ").strip().title()
            if userinput in dictionary:
                cost = cost + dictionary[userinput]
                print(f"Total: ${cost:.2f}")
        except:
            print("")
            break




main()
