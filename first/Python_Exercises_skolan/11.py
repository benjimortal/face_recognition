def dict_():
    n = input('enter a number: \n')
    d = {}
    for i in range(1, int(n),+1):
        d[i] = i*i
    print(d)

def main():
    dict_()


if __name__ == '__main__':
    main()
