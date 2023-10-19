import random


def jogar():

    imprime_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = ['_' for letra in palavra_secreta]
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1
            print(f"Ops, você errou! Faltam {7 - tentativas} tentativas.")

        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra
        index += 1


def pede_chute():
    chute = input('Qual letra? ')
    chute = chute.strip().upper()
    return chute


def imprime_abertura():
    print("Bem vindo ao jogo de FORCA!")


def carrega_palavra_secreta(nome_arquivo='palavras.txt'):
    arquivo = open(nome_arquivo, encoding='utf-8', mode='r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def imprime_mensagem_vencedor():
    print('Parabéns!!! Você ganhou!!!')


def imprime_mensagem_perdedor(palavra_secreta):
    print('Você perdeu!!!')
    print(f'A palavra era {palavra_secreta}')


if __name__ == "__main__":
    jogar()
