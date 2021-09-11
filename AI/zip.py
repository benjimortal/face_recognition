def main():
    list_a = [1,2,3,4,5]
    list_b = ['a','b','c','d','e']

    #print(list(zip(list_a,list_b)))
    for e, l in zip(list_a,list_b):
        print(e,'==>', l)

    # d = {e: l for e, l in zip(list_a,list_b)}
    # print(d)


if __name__ == '__main__':
    main()
