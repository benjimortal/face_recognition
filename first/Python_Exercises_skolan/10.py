def fined_the_number():
    for n in range(2000, 3201):
        if n % 7 == 0 and n % 5 != 0:
            print(n,',', end='')


def main():
    fined_the_number()


if __name__ == '__main__':
    main()
