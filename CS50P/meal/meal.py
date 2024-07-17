def main():
    timeinput = input("What time is it? ").lower().strip()
    timeinput = convert(timeinput)
    if timeinput >= 7 and timeinput <= 8:
        print("breakfast time")
    if timeinput >= 12 and timeinput <= 13:
        print("lunch time")
    if timeinput >= 18 and timeinput <= 19:
        print("dinner time")
    else:
        exit()

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    added_hours = minutes / 60
    return hours + added_hours

if __name__ == "__main__":
    main()
