def is_vowel(char):
    vowels = 'aeiouy'
    if char.lower() in vowels:
        return True
    else:
        return False


def main():
    if is_vowel('A'):
        print('yes')
    else:
        print('no')
    if is_vowel('A'):
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()
