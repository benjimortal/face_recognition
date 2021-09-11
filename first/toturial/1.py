calculation_to_units = 24
name_of_unit = 'hours'

def days_to_units(num_of_days):
    print(num_of_days > 0) # True or False if it is positive or negative
    if num_of_days > 0:
        return f"{name_of_unit} days are {num_of_days * calculation_to_units} {name_of_unit}"
    else:
        return f'Please enter a positive number!'


def main():
    user_input =(input('Enter the hour: '))
    user_input_number = int(user_input)
    calculate_value = days_to_units(user_input_number)
    print(calculate_value)



if __name__ == '__main__':
    main()
