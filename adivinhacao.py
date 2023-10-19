from random import randint


def jogar():
    print('Bem vindo ao jogo de Adivinhação!')

    numero_secreto = randint(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade? ')
    print('[1] FÁCIL\n'
          '[2] MÉDIO\n'
          '[3] DIFÍCIL\n')

    nivel = int(input('Defina o nível: '))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 14
    else:
        total_de_tentativas = 7

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentaviva {rodada} de {total_de_tentativas}')
        chute = int(input('Digite um número entre 1 e 100: '))
        print('Você digitou: ', chute)

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100!')
            continue
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f'Você acertou e fez {pontos} pontos!')
            break
        else:
            if maior:
                print('Você errou! O seu chute foi MAIOR que o número.')
            elif menor:
                print('Você errou! Seu chute foi MENOR que o número.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print(f'O número secreto era {numero_secreto}')
    print('FIM DO JOGO.')


if __name__ == "__main__":
    jogar()
