from sys import argv

def str_to_morse(join):
    morse_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}
    for i in join:
        if i.isalnum():
            print(morse_dict[i], end='')
        else:
            print(" /", end='')
        print(' ', end='')
    print()
    

if __name__ == '__main__':
    separator = " "
    argv.pop(0)[0]
    for i in argv:
        for j in i:
            if (j.isalnum() == False and j.isspace() == False):
                print(j)
                print('ERROR')
                exit(2)
    join = separator.join(argv)
    str_to_morse(join.upper())