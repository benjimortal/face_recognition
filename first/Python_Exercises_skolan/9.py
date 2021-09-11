def text():
    vowels = 'aeiouy'
    user = input('Please write something here: \n')

    for i in user:
        if i in vowels:
            print(i.upper())
        print(i)


def main():
    text()


if __name__ == '__main__':
    main()
