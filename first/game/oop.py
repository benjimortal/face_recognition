class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name

        self.email = email

    def jump(self):
        print(self.first_name,self.last_name, 'is jumping!')

    def info(self):
        print(f'It is {self.first_name} {self.last_name} and you can contact me by: {self.email}')

def main():
    p1 = Person('Anna', 'Svenson', 'anna@gmail.com')
    p2 = Person('Kalle', 'Karlsson', 'kalle@gmail.com')
    p1.jump()
    p2.info()


if __name__ == '__main__':
    main()
