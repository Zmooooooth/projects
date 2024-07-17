import requests
import sys
import json

def main():
    inputfloat = check_argument()
    floatvalbtcUSD = get_data()
    yourprice = inputfloat * floatvalbtcUSD
    string = f"${yourprice:,.4f}"
    print(string)
    #print(floatvalbtcUSD)

def get_data():
    try:
        jsonanswer = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        answer = jsonanswer.json()
    except requests.RequestException:
        sys.exit("System Error")
    items = json.dumps(answer, indent=2)
    data = json.loads(items)
    btc_value_USD = data['bpi']['USD']['rate_float']
    return float(btc_value_USD)

def check_argument():
    try:
        result = sys.argv[1]
    except:
        sys.exit("Missing command-line argument")
    try:
        return float(result)
    except:
        sys.exit("Command-line argument is not a number")
if __name__ == "__main__":
    main()
