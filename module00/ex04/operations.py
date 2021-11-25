import sys

def operations(nbr1, nbr2):
    'Usage: python operations.py <numbers1> <numbers2>\nExample:\n\tpython operations 12 3'
    print('{0: <12}'.format('Sum:') + str(int(nbr1) + int(nbr2)))
    print('{0: <12}'.format('Difference:') + str(int(nbr1) - int(nbr2)))
    try:
        print('{0: <12}'.format('Quotient:') + str(float(nbr1) / float(nbr2)))
    except:
        print('{0: <12}'.format('Quotient:') + "ERROR (Div by zero)")
    try:
        print('{0: <12}'.format('Remainder:') + str(int(nbr1) % int(nbr2)))
    except:
        print('{0: <12}'.format('Remainder:') + "ERROR (Mod vy zero)")

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        if (len(sys.argv) != 1):
            print("InputError: too many arguments")
        print(operations.__doc__)
        exit(2)
    try:
        int(sys.argv[1]), int(sys.argv[2])
    except:
        print("InputError: Only numbers\n\n" + operations.__doc__)
        exit(2)
    operations(sys.argv[1], sys.argv[2])