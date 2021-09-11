def max_of_three(first,second,third):
    if first > second and first > third:
        return first
    elif second > third:
        return second
    else:
        return third

def main():
    the_biggest_num = max_of_three(20,30,50)
    print(the_biggest_num)


if __name__ == '__main__':
    main()
