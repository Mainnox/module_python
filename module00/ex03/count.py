
def isupper(c):
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    if (upper.find(c) != -1):
        return (1)
    return (0)

def islower(c):
    lowerw = "qwertyuiopasdfghjklzxcvbnm"
    if (lowerw.find(c) != -1):
        return (1)
    return (0)

def ispunc(c):
    punc = ",.!?'\";:-_"
    if (punc.find(c) != -1):
        return (1)
    return (0)

def text_analyzer(string):
    'This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'
    space = 0
    upper = 0
    lower = 0
    punc = 0
    for i in range(0, len(string)):
        if (string[i] == ' '):
            space += 1
        upper += isupper(string[i])
        lower += islower(string[i])
        punc += ispunc(string[i])
    print("The text contains " + str(len(string)) + " characters:\n- " + str(upper) + " upper letters\n- " + str(lower) + " lower letters\n- " + str(punc) +" punctuation mark\n- " + str(space) + " spaces")