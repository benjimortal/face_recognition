import random


def main():
    största = int(input('Det största möjliga talet? '))
    försök = int(input('Hur många försök får man? '))
    tal = random.randint(1, största)

    for i in range(försök):
        gissning = int(input('Gissa talet? '))
        if gissning < tal:
            print('För litet')
        elif gissning > tal:
            print('För stort')
        else:
            print('Rätt gissning! ')
            break
    else:
        print('Inga fler försök')
        print('Talet var: ', tal)

if __name__ == '__main__':
    main()
