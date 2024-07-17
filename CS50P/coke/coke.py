def main():
    price_of_coke = 50
    payed = False
    acceptable_coins = [0,5,10,25]
    while payed == False:
        user_cash_input = int(input("Insert Coin: "))
        if check_for_right_input(user_cash_input,acceptable_coins) == True:
            price_of_coke = price_of_coke - user_cash_input
            if price_of_coke < 0:
                print(f"Change Owed: {price_of_coke * -1}")
                payed = True
                break
            if price_of_coke == 0:
                print(f"Change Owed: {price_of_coke}")
                payed = True
                break
            else:
                print(f"Amount Due: {price_of_coke}")
        else:
            print(f"Amount Due: {price_of_coke}")

def check_for_right_input(input,list):
    status = False
    for coin in list:
        if input == coin:
            status = True
    return status

main()
