import sys

arguments = sys.argv[1:]

if __name__ == "__main__":
    if arguments:
        print("Hello", ' '.join(arguments[::]), "!")
    else:
        print("Hello World!")
