def max_func(first, second):
    if first > second:
        return first
    else:
        return second


def main():
    biggest = max_func(4, 9)
    print(biggest)


if __name__ == '__main__':
    main()
