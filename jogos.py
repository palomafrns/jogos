import forca
import adivinhacao


def escolha_jogo():
    print('ESCOLHA O SEU JOGO')

    print('[1] Adivinhação\n'
          '[2] Forca')
    jogo = int(input('Qual jogo? '))

    if jogo == 1:
        print('Jogando adivinhação')
        adivinhacao.jogar()
    elif jogo == 2:
        print('Jogando forca')
        forca.jogar()


if __name__ == "__main__":
    escolha_jogo()
