import sys

if (__name__ == "__main__"):
    if (len(sys.argv) != 2):
        exit(2)
    if (sys.argv[1].isdigit() == False):
        print("ERROR")
        exit(2)
    number = int(sys.argv[1])
    if (number == 0):
        ret = "Zero"
    elif (number % 2 == 0):
        ret = "Even"
    else:
        ret = "Odd"
    print("I'm " + ret + ".")