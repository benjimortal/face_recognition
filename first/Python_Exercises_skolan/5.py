def main():
    age = int(input('Enter your age: '))
    print(f'Your age is {age}!')
    if age < 18:
        print('You are a teen! ')
    else:
        print('You are adult! ')


if __name__ == '__main__':
    main()
