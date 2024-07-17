def main():
    month_dict = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    get_user_input(month_dict)

def get_user_input(month_dict):
    while True:
        try:
            user_input = input("Date: ")
        except EOFError:
            break

        if "/" in user_input:
            if process_date_with_slash(user_input):
                break
        elif "," in user_input:
            if process_date_with_comma(user_input, month_dict):
                break
        else:
            continue

def process_date_with_slash(date_str):
    try:
        month, day, year = date_str.split("/")
        day, month, year = int(day), int(month), int(year)
        if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
            print(f"{year:04}-{month:02}-{day:02}")
            return True
    except ValueError:
        pass
    return False

def process_date_with_comma(date_str, month_dict):
    try:
        month_day, year = date_str.split(", ")
        month_name, day = month_day.split(" ")
        day, year = int(day), int(year)
        month = month_dict.get(month_name)
        if month and 1 <= day <= 31 and year > 0:
            print(f"{year}-{month}-{day:02}")
            return True
    except:
        pass
    return False

main()
