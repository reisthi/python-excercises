import sys


arguments = sys.argv[1]
if __name__ == "__main__":
    if arguments:
        one = format(sys.argv[1])
        two = format(sys.argv[2])
        # print(one, two)
        if one > two:
            print(one, " is bigger than ", two)
        elif two > one:
            print(two, " is bigger than ", one)
        else:
            print("They are equal.")



