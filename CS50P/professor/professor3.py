import random
import sys

def main():
    user_level = get_level()
    score = 0

    # Game logic
    for index in range(10):
        q_solved = False
        wrong_counter = 0
        x, y, solution = generate_question(user_level)

        while not q_solved:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                wrong_counter += 1
                print("EEE")
                if wrong_counter == 3:
                    print(f"{x} + {y} = {solution}")
                    break
            else:
                if answer == solution:
                    score += 1
                    q_solved = True
                else:
                    wrong_counter += 1
                    print("EEE")
                    if wrong_counter == 3:
                        print(f"{x} + {y} = {solution}")
                        break

    print(f"Score: {score}")
    sys.exit()

def get_level():
    while True:
        try:
            inp = int(input("Level: "))
            if inp not in [1, 2, 3]:
                continue
        except ValueError:
            continue
        else:
            return inp

def generate_question(level):
    x = generate_integer(level)
    y = generate_integer(level)
    solution = x + y
    return x, y, solution

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
