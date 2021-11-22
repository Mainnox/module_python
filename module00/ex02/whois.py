import sys

if (__name__ == "__main__"):
    if (len(sys.argv) != 2):
        exit(2)
    print(sys.argv[1].isdigit)
    print("Tout finis !")
