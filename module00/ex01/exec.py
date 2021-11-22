import sys

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print("Usage: python exec.py [args]")
        exit(2)
    sys.argv.remove("exec.py")
    s = ""
    for i in sys.argv:
        if (len(s)):
            s += ' '
        s += i
    s = s.swapcase()
    print(s[::-1])