from sys import argv

if __name__ == '__main__':
    if (len(argv) != 3):
        print('ERROR')
        exit(2)
    try:
        int(argv[2])
    except:
        print('ERROR')
        exit(2)
    l = argv[1].split()
    ret = []
    print(l)
    for i in l:
        if (len(i) > int(argv[2])):
            ret.append(i)
    print(ret)