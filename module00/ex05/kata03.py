import sys

if __name__ == "__main__":
    phrase = "The right format"
    sys.stdout.write('{:->42}'.format(phrase))