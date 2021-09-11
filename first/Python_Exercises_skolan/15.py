def myLen(iterable):
    counter = 0
    for x in iterable:
        counter += 1
    return counter


def main():
    mystr = "hello there my friend"
    print(myLen(mystr))

    mylist = [1,2,3,4,5,6,7]
    print(myLen(mylist))


if __name__ == '__main__':
    main()


# def myLen(iterable):
#     counter = 0
#     for x in iterable:
#         counter += 1
#     return counter
#
#
# def main():
#     myStr = "Hello there my friend"
#     print(myLen(myStr))




if __name__ == '__main__':
    main()