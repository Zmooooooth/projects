import random
import sys

def main():
    #initiation
    user_level = get_level()
    dict_q = generate_questions(user_level)
    score = 0
    #print(dict_q)
    #gamelogic
    for question in dict_q:
        q_solved = False
        wrong_counter = 0
        while q_solved == False:
            answer = input(question)
            if answer == str(dict_q[question]):
                score += 1
                q_solved = True
            elif wrong_counter == 2:
                print("EEE")
                print(f"{question}{dict_q[question]}")
                break
            else:
                wrong_counter += 1
                print("EEE")
    print(f"Score: {score}")
    sys.exit()
def get_level():
    while True:
        try:
            inp = int(input("Level: "))
            if inp not in [1,2,3]:
                continue
        except ValueError:
            pass
        else:
            return inp

def generate_questions(level):
    question_dict = {}
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        solution = x + y
        question_dict[f"{x} + {y} = "] = solution
    return question_dict

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
