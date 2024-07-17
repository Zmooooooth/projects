import yfinance as yf
import csv
import tabulate
from pyfiglet import Figlet


def main():
    actions = [
        ["Key", "Usage", "Description"],
        ["b", "Buy Stock", "Buy a stock and add it to your portfolio"],
        ["s", "Sell Stock", "Sell a stock and remove it from your portfolio"],
        ["o", "Show Portfolio", "Get insight into gains and losses of your portfolio"],
        ["e", "Exit", "Save and close the program"]
    ]

    portfolio = retrieve_stocks("portfolio.csv")

    f = Figlet(font='slant')
    print("\n")
    print(f.renderText("TERMINAL PORTFOLIO MANAGER"))

    while True:
        show_startpage(actions)
        result = await_userinput()
        if result == "e":
            save_to_csv(portfolio, filename="portfolio.csv")
            break
        elif result == "b":
            portfolio = buy_stock(portfolio)
            save_to_csv(portfolio, filename="portfolio.csv")
        elif result == "o":
            show_portfolio(portfolio)
        elif result == "s":
            portfolio = sell_stock(portfolio)
            save_to_csv(portfolio, filename="portfolio.csv")

def show_startpage(start_list):
    res = tabulate.tabulate(start_list[1:], start_list[0], tablefmt="fancy_outline")
    print(res)

def search_stock(stock_shortage):
    try:
        stock = yf.Ticker(stock_shortage.upper())
        price = stock.history(period='1d')['Close'].iloc[0]
        return price
    except Exception as e:
        print(f"Error: {e}")
    return None

def retrieve_stocks(filename):
    portfolio = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                portfolio.append({
                    "abbreviation": line["abbreviation"].strip(),
                    "amount_of_stock": float(line["amount_of_stock"].strip()),
                    "price_payed": float(line["price_payed"].strip())
                })
    except:
        with open(filename, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["abbreviation", "amount_of_stock", "price_payed"])
            writer.writeheader()
    return portfolio

def get_valid_float(question):
    while True:
        try:
            userin = float(input(question))
            if userin > 0:
                return userin
        except ValueError:
            print("Invalid floating point number")

def buy_stock(dictionary_list):
    header_list = ["Abbreviation", "Price", "Amount"]
    input_list = ["---", "---", "---"]
    style_list = [header_list, input_list]

    while True:
        user_input_abbr = input(tabulate.tabulate(style_list[1:], headers=style_list[0], tablefmt="fancy_outline") + "\nPlease enter the Abbreviation:").strip().upper()
        price = search_stock(user_input_abbr)
        if price is not None:
            break
        else:
            print("Invalid Abbreviation")

    input_list[0] = user_input_abbr
    user_input_price = get_valid_float(tabulate.tabulate(style_list[1:], headers=style_list[0], tablefmt="fancy_outline") + "\nPlease enter the overall price you payed in $:")
    input_list[1] = f"${user_input_price}"
    user_input_amount = get_valid_float(tabulate.tabulate(style_list[1:], headers=style_list[0], tablefmt="fancy_outline") + "\nPlease enter the amount of stocks you purchased:")
    input_list[2] = user_input_amount

    for dictionary in dictionary_list:
        if dictionary["abbreviation"] == user_input_abbr:
            dictionary["amount_of_stock"] += user_input_amount
            dictionary["price_payed"] += user_input_price
            return dictionary_list

    new_dictionary = {
        "abbreviation": user_input_abbr,
        "amount_of_stock": user_input_amount,
        "price_payed": user_input_price
    }
    dictionary_list.append(new_dictionary)
    return dictionary_list

def show_portfolio(portfolio):
    header = ["Abbreviation", "Amount of Stock", "Price Payed", "Current Value", "Result"]
    rows = []
    for stock in portfolio:
        content = []
        content.append(stock["abbreviation"])
        content.append(stock["amount_of_stock"])
        content.append(f"${stock['price_payed']:,.2f}")
        curr_value = search_stock(stock["abbreviation"]) * stock["amount_of_stock"]
        content.append(f"${curr_value:,.2f}")
        result = curr_value - stock["price_payed"]
        if result > 0:
            content.append(f"+ ${result:,.2f}")
        else:
            content.append(f"- ${(result * -1):,.2f}")
        rows.append(content)
    print(tabulate.tabulate(rows, headers=header, tablefmt="fancy_outline"))
    return True

def sell_stock(dictionary_list):
    header = ["Abbreviation", "Total Amount", "Amount to Sell"]
    input_list = ["---", "---", "---"]
    style_list = [header, input_list]
    stock_found = False

    while not stock_found:
        user_input_abbr = input(tabulate.tabulate(style_list[1:], headers=style_list[0], tablefmt="fancy_outline") + "\nPlease enter the Abbreviation of the stock to sell: ").strip().upper()

        for dictionary in dictionary_list:
            if user_input_abbr == dictionary["abbreviation"]:
                stock_found = True
                input_list[0] = dictionary["abbreviation"]
                input_list[1] = dictionary["amount_of_stock"]
                break
        if not stock_found:
            print("Stock not in portfolio. Please try again.")

    while True:
        user_input_amount = get_valid_float(tabulate.tabulate(style_list[1:], headers=style_list[0], tablefmt="fancy_outline") + "\nPlease enter the amount of stocks you want to sell: ")
        if user_input_amount <= dictionary["amount_of_stock"]:
            input_list[2] = user_input_amount
            break
        else:
            print("Not enough stock to sell. Please enter a valid amount.")

    for dictionary in dictionary_list:
        if dictionary["abbreviation"] == user_input_abbr:
            header = ["Abbreviation", "Sold Amount", "Sold Value", "Result"]
            curr_value = search_stock(dictionary["abbreviation"])
            sold_value = user_input_amount * curr_value
            result_sell = (curr_value - (dictionary["price_payed"] / dictionary["amount_of_stock"])) * user_input_amount

            if (dictionary["price_payed"] / dictionary["amount_of_stock"]) > curr_value:
                result_type = "Loss"
                header[3] = result_type
                row = [dictionary["abbreviation"], user_input_amount, f"${(sold_value * 1):,.2f}", f"- ${(result_sell * -1):,.2f}"]
            else:
                result_type = "Profit"
                header[3] = result_type
                row = [dictionary["abbreviation"], user_input_amount, f"${sold_value:,.2f}", f"+ ${result_sell:,.2f}"]

            # Update price_payed before updating amount_of_stock to avoid ZeroDivisionError
            dictionary["price_payed"] -= (dictionary["price_payed"] / dictionary["amount_of_stock"]) * user_input_amount
            dictionary["amount_of_stock"] -= user_input_amount

            if dictionary["amount_of_stock"] == 0:
                dictionary_list.remove(dictionary)

            print(tabulate.tabulate([row], headers=header, tablefmt="fancy_outline"))
            return dictionary_list

    return dictionary_list

def save_to_csv(dictionary_list, filename):
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["abbreviation", "amount_of_stock", "price_payed"])
        writer.writeheader()
        for dictionary in dictionary_list:
            writer.writerow(dictionary)

def await_userinput():
    while True:
        userin = input("Please enter: ").strip().lower()
        if userin in ["b", "s", "o", "e"]:
            return userin
        else:
            print("Invalid command, please try again")

if __name__ == "__main__":
    main()
