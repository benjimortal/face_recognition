calculation_to_units = 24
name_of_unit = 'hours'

def days_to_units(num_of_days, custom_message):
    print(f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}')
    print(custom_message)


def main():
    days_to_units(20, 'are you happy now?')


if __name__ == '__main__':
    main()
