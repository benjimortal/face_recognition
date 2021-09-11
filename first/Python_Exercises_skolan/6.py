def main():
    notes = {
            '1' : 'George Washington',
            '2' : 'Thomas Jefferson',
            '5' : 'Abraham',
            '10': 'Alexander Hamilton',
            '20': 'Ulysses S.Grant',
            '50': 'Andrew Jackson',
            '100':'Benjamin Franklin'
     }
    value = input('Please enter the value of an US dollar note: ')
    if value not in notes:
        print('Sorry that is not a valid US dollar note.')
    else:
        print(f'On that note you will find', notes[value])

if __name__ == '__main__':
    main()
