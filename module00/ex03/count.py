
def isupper(c):
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    if (upper.find(c) != -1):
        return (1)
    return (0)

def islower(c):
    lowerw = "qwertyuiopadfghjklzxcvbnm"
    if (lowerw.find(c) != -1):
        return (int(1))
    return (int(0))

def ispunc(c):
    punc = ",.?'\";:-_"
    if (punc.find(c) != -1):
        return (1)
    return (0)


def text_analyzer(string):
    'This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'
    space = 0
    upper = int(0)
    lower = 0
    punc = 0

    for i in enumerate(string):
           if (string[i] == ' '):
               space += 1
            upper += isupper(string[i])
            lower += islower(string[i])
            punc += ispunc(string[i])
    print("" + upper + lower + punc + space)
    exit(0)