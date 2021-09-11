def main():
    vowels = 'aeiouy'
    char = input('Enter a character: ')
    if char.lower() in vowels:
        print(char, 'is a vowel')
    else:
        print(char, 'is not vowel')

if __name__ == '__main__':
    main()
