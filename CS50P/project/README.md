# TERMINAL PORTFOLIO MANAGER
    #### Video Demo: https://youtu.be/XZGRd3RI4Uo
    #### Description:

    With Terminal Portfolio Manager you are able to keep track of your stock-picks during all times!

![Start Page of Terminal Portfolio Manager](https://i.ibb.co/yFLDn0n/Screenshot-2024-05-30-152707.png)

# How the System works
    Terminal Portfolio Manager is connected to the Yahoo-Finance API.

    This ensures up to date data about each stock in your portfolio.

    Your portfolio is stored in a csv-file called "portfolio.csv"

    You can delete this file without any problems, the program is going to rebuilt it!

# Design Choice Terminal Window
    Terminal windows are the easiest way to output information for the user.

    The Terminal Window can look decent combined with modules like:

* tabulate
* pyfiglet

# Requirements
    pip install tabulate
    pip install csv
    pip install yfinance
    pip install pyfiglet

# Usage
    with [o] show portfolio

    with [s] sell a specific stock of your portfolio

    with [b] add a stock to your portfolio

    you can exit and save with [e]


!["Portfolio Overview"](https://i.ibb.co/nbQ1Tjb/o.png)
!["Portfolio b"](https://i.ibb.co/FmYWmGF/b.png)
!["Portfolio s"](https://i.ibb.co/v4rYkqN/s.png)

# Methods
    show_startpage(start_list)

    Takes the start-list as an argument in order to show a tabulate list.



    search_stock(abbr)

    Takes the short index form of a stock as argument and returns the price of it with use of the Yahoo-Finance API



    retrieve_stocks(filename)

    Takes a filename as argument and returns a dictionary of the file's content.
    The file MUST be a csv file.



    get_valid_float(question)

    Takes a string as the input question and reprompts the user until a valid float is inputted.
    Returns the float.



    buy_stock(dictionary)

    Takes the data dictionary as input and adds a stock based on validity and the user's input.
    Returns a modified version of the data dictionary.



    show_portfolio(dictionary)

    Takes the data dictionary and prints a table of all stocks, amount, buy-price and current value.



    save_to_csv(dictionary,filename)

    Takes the data dictionary and saves it to a csv file with the filename.



    await_userinput()

    This method ensures that the user only operates the main page with the keys: [b] [s] [o] [e]

# Other Files
    test_project.py tests the methodes of project.py
