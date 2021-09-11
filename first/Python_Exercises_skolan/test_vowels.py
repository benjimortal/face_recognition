def vowels_to_upper(text):
    vowels = "aeiouy"
    newStr = ""
    for c in text:
        if c in vowels:
            newStr += c.upper()
        else:
            newStr += c
    return newStr


def main():
    print(vowels_to_upper("hi there. this is a great program"))


if __name__ == '__main__':
    main()