def hello(first_name, last_name, age):
    print('hello world!',  first_name, last_name)
    print('have a nice day')
    print(f'{first_name}, {last_name} you are {age} years old.')



def main():
    name = 'Jawid'
    family = 'Mortazawi'
    age = 25
    hello(name, family, age)



if __name__ == '__main__':
    main()
