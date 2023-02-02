import random

def generator():
    exit = False
    while not exit:
        print('Seja bem-vindo ao nosso gerador de números aleatórios')
        print('1. Gerar')
        print('2. Sair')

        choice = int(input(''))

        if choice == 1:
            number = random.randrange(0,101)
            print(f'Número gerado: {number}')
        
        elif choice == 2:
            exit = True
            print('Até a próxima!')
        
        else:
            print('Opção inexistente')
            generator()
        
generator()