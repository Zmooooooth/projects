import requests
import sys
#import json
import mymodule

def main():
    integer = mymodule.getuser_int_positive("How many results do u want? ")
    if len(sys.argv) < 2:
        sys.exit()
    else:
        url = f"https://itunes.apple.com/search?entity=song&limit=1&term=weezer"
        answer = requests.get(f"https://itunes.apple.com/search?entity=song&limit={integer}&term={sys.argv[1]}")
        o = answer.json()
        for result in o["results"]:
            print(result["trackName"])

main()
