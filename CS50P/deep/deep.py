str_in = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
match str_in:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

