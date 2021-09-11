def main():
    for n in range(1000, 3001):
        str_num = str(n)
        split_str = list(str_num)
        all_even = True
        for x in split_str:
            if int(x) % 2 != 0:
                all_even = False
        if all_even:
            print(n, ',', end='')


if __name__ == '__main__':
    main()
