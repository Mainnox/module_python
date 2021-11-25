import sys

def operations(nbr1, nbr2):
    'Usage: python operations.py <numbers1> <numbers2>\nExample:\n\tpython operations 12 3'

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("InputError: too many arguments")
        print(operations.__doc__)
    print(type(sys.argv[1]), type(sys.argv[2]))