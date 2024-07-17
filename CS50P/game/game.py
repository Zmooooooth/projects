import mymodule
import random

def main():
    nlevel = mymodule.getuser_int_positive("Level: ")
    randomnumber = random.randint(1,nlevel)
    solved = False
    while solved == False:
        userguess = mymodule.getuser_int_positive("Guess: ")
        if userguess < randomnumber:
            print("Too small!")
        elif userguess > randomnumber:
            print("Too large!")
        else:
            print("Just right!")
            solved == True
            break


if __name__ == "__main__":
    main()
