'''
Trabalho - 2
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''

import cv2
import numpy as np
import argparse

def MetodoFloydSteinberg(imagem, erro, i, j, invertido):
    if not invertido:
        # Propagação do erro normal
        # Primeira linha
        imagem[i][j + 1] = imagem[i][j + 1] + (7 / 16) * erro

        # Segunda linha
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (3 / 16) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (5 / 16) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (1 / 16) * erro
    else:
        # Propagação do erro invertida
        # Primeira linha
        imagem[i][j - 1] = imagem[i][j - 1] + (7 / 16) * erro

        # Segunda linha
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (3 / 16) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (5 / 16) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (1 / 16) * erro

def MetodoStevensonArce(imagem, erro, i, j, invertido):
    if not invertido:
        # Propagação do erro normal
        # Primeira linha
        imagem[i][j + 2] = imagem[i][j + 2] + (32 / 200) * erro

        # Segunda linha
        imagem[i + 1][j - 3] = imagem[i + 1][j - 3] + (12 / 200) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (26 / 200) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (30 / 200) * erro
        imagem[i + 1][j + 3] = imagem[i + 1][j + 3] + (16 / 200) * erro

        # Terceira linha
        imagem[i + 2][j - 2] = imagem[i + 2][j - 2] + (12 / 200) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (26 / 200) * erro
        imagem[i + 2][j + 2] = imagem[i + 2][j + 2] + (12 / 200) * erro

        # Quarta linha
        imagem[i + 3][j - 3] = imagem[i + 3][j - 3] + (5 / 200) * erro
        imagem[i + 3][j - 1] = imagem[i + 3][j - 1] + (12 / 200) * erro
        imagem[i + 3][j + 1] = imagem[i + 3][j + 1] + (12 / 200) * erro
        imagem[i + 3][j + 3] = imagem[i + 3][j + 3] + (5 / 200) * erro

    else:

        # Propagação do erro invertido
        # Primeira linha
        imagem[i][j - 2] = imagem[i][j - 2] + (32 / 200) * erro

        # Segunda linha
        imagem[i + 1][j + 3] = imagem[i + 1][j + 3] + (12 / 200) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (26 / 200) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (30 / 200) * erro
        imagem[i + 1][j - 3] = imagem[i + 1][j - 3] + (16 / 200) * erro

        # Terceira linha
        imagem[i + 2][j + 2] = imagem[i + 2][j + 2] + (12 / 200) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (26 / 200) * erro
        imagem[i + 2][j - 2] = imagem[i + 2][j - 2] + (12 / 200) * erro

        # Quarta linha
        imagem[i + 3][j + 3] = imagem[i + 3][j + 3] + (5 / 200) * erro
        imagem[i + 3][j + 1] = imagem[i + 3][j + 1] + (12 / 200) * erro
        imagem[i + 3][j - 1] = imagem[i + 3][j - 1] + (12 / 200) * erro
        imagem[i + 3][j - 3] = imagem[i + 3][j - 3] + (5 / 200) * erro

def MetodoBurkes(imagem, erro, i, j, invertido):
    if not invertido:

        # Propagação do erro normal
        # Primeira linha
        imagem[i][j + 1] = imagem[i][j + 1] + (8 / 32) * erro
        imagem[i][j + 2] = imagem[i][j + 2] + (4 / 32) * erro

        # Segunda linha
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (2 / 32) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (4 / 32) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (8 / 32) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (4 / 32) * erro
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (2 / 32) * erro

    else:

        # Propagação do erro invertido
        # Primeira linha
        imagem[i][j - 1] = imagem[i][j - 1] + (8 / 32) * erro
        imagem[i][j - 2] = imagem[i][j - 2] + (4 / 32) * erro

        # Segunda linha
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (2 / 32) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (4 / 32) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (8 / 32) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (4 / 32) * erro
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (2 / 32) * erro

def MetodoSierra(imagem, erro, i, j, invertido):

    if not invertido:

        # Propagação do erro normal
        # Primeira linha
        imagem[i][j + 1] = imagem[i][j + 1] + (5 / 32) * erro
        imagem[i][j + 2] = imagem[i][j + 2] + (3 / 32) * erro

        # Segunda linha
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (2 / 32) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (4 / 32) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (5 / 32) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (4 / 32) * erro
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (2 / 32) * erro

        # Terceira linha
        imagem[i + 2][j - 1] = imagem[i + 2][j - 1] + (2 / 32) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (3 / 32) * erro
        imagem[i + 2][j + 1] = imagem[i + 2][j + 1] + (2 / 32) * erro

    else:

        # Propagação do erro invertido
        # Primeira linha
        imagem[i][j - 1] = imagem[i][j - 1] + (5 / 32) * erro
        imagem[i][j - 2] = imagem[i][j - 2] + (3 / 32) * erro

        # Segunda linha
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (2 / 32) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (4 / 32) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (5 / 32) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (4 / 32) * erro
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (2 / 32) * erro

        # Terceira linha
        imagem[i + 2][j + 1] = imagem[i + 2][j + 1] + (2 / 32) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (3 / 32) * erro
        imagem[i + 2][j - 1] = imagem[i + 2][j - 1] + (2 / 32) * erro

def MetodoStucki(imagem, erro, i, j, invertido):

    if not invertido:

        # Propagação do erro normal
        # Primeira linha
        imagem[i][j + 1] = imagem[i][j + 1] + (8 / 42) * erro
        imagem[i][j + 2] = imagem[i][j + 2] + (4 / 42) * erro

        # Segunda linha
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (2 / 42) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (4 / 42) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (8 / 42) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (4 / 42) * erro
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (2 / 42) * erro

        # Terceira linha
        imagem[i + 2][j - 2] = imagem[i + 2][j - 2] + (1 / 42) * erro
        imagem[i + 2][j - 1] = imagem[i + 2][j - 1] + (2 / 42) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (4 / 42) * erro
        imagem[i + 2][j + 1] = imagem[i + 2][j + 1] + (2 / 42) * erro
        imagem[i + 2][j + 2] = imagem[i + 2][j + 2] + (1 / 42) * erro

    else:

        # Propagação do erro normal
        # Primeira linha
        imagem[i][j - 1] = imagem[i][j - 1] + (8 / 42) * erro
        imagem[i][j - 2] = imagem[i][j - 2] + (4 / 42) * erro

        # Segunda linha
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (2 / 42) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (4 / 42) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (8 / 42) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (4 / 42) * erro
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (2 / 42) * erro

        # Terceira linha
        imagem[i + 2][j + 2] = imagem[i + 2][j + 2] + (1 / 42) * erro
        imagem[i + 2][j + 1] = imagem[i + 2][j + 1] + (2 / 42) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (4 / 42) * erro
        imagem[i + 2][j - 1] = imagem[i + 2][j - 1] + (2 / 42) * erro
        imagem[i + 2][j - 2] = imagem[i + 2][j - 2] + (1 / 42) * erro

def MetodoJarvisJudiceNinke(imagem, erro, i, j, invertido):

    if not invertido:

        # Propagação do erro normal
        # Primeira linha
        imagem[i][j + 1] = imagem[i][j + 1] + (7 / 48) * erro
        imagem[i][j + 2] = imagem[i][j + 2] + (5 / 48) * erro

        # Segunda linha
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (3 / 48) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (5 / 48) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (7 / 48) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (5 / 48) * erro
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (3 / 48) * erro

        # Terceira linha
        imagem[i + 2][j - 2] = imagem[i + 2][j - 2] + (1 / 48) * erro
        imagem[i + 2][j - 1] = imagem[i + 2][j - 1] + (3 / 48) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (5 / 48) * erro
        imagem[i + 2][j + 1] = imagem[i + 2][j + 1] + (3 / 48) * erro
        imagem[i + 2][j + 2] = imagem[i + 2][j + 2] + (1 / 48) * erro

    else:

        # Propagação do erro normal
        # Primeira linha
        imagem[i][j - 1] = imagem[i][j - 1] + (7 / 48) * erro
        imagem[i][j - 2] = imagem[i][j - 2] + (5 / 48) * erro

        # Segunda linha
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (3 / 48) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (5 / 48) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (7 / 48) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (5 / 48) * erro
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (3 / 48) * erro

        # Terceira linha
        imagem[i + 2][j + 2] = imagem[i + 2][j + 2] + (1 / 48) * erro
        imagem[i + 2][j + 1] = imagem[i + 2][j + 1] + (3 / 48) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (5 / 48) * erro
        imagem[i + 2][j - 1] = imagem[i + 2][j - 1] + (3 / 48) * erro
        imagem[i + 2][j - 2] = imagem[i + 2][j - 2] + (1 / 48) * erro

def DifusaoDeErro(imagem, alternado, pad, mascara, camadas):
    imagemOriginal = np.copy(imagem)
    imagemX, imagemY = imagemOriginal.shape[0:2]
    imagemOriginal = cv2.copyMakeBorder(imagemOriginal, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0) # aplicação de padding zero com largura do tamanho do pad
    imagemResultado = np.zeros((imagemX, imagemY, camadas), dtype=np.uint8) # resultado
    imagemOriginal = imagemOriginal.astype(np.float64)
    flag = True

    for i in range(pad, imagemX + pad):
        if flag:
            for j in range(pad, imagemY + pad):
                pixels = np.copy(imagemOriginal[i][j])
                pixels = np.where(pixels < 128, 0, 255)
                erro = np.subtract(imagemOriginal[i][j], pixels)

                mascara(imagemOriginal, erro, i, j, False)

                imagemResultado[i - pad][j - pad] = pixels
                if alternado:
                    flag = False
        else:
            for j in range(imagemY-1+pad, pad, -1):
                pixels = np.copy(imagemOriginal[i][j])
                pixels = np.where(pixels < 128, 0, 255)
                erro = np.subtract(imagemOriginal[i][j], pixels)

                mascara(imagemOriginal, erro, i, j, True)

                imagemResultado[i - pad][j - pad] = pixels
                flag = True

    return imagemResultado


#Nome dos arquivos de saida
def ArquivoDeSaida(nomeDoMetodo, alternado):
    if alternado:
        return f'outputs/trabalho_2_{nomeDoMetodo}_alternado.png'

    return f'outputs/trabalho_2_{nomeDoMetodo}.png'


#Constantes - Mascaras para utilizar
MASCARAS = np.array([['FloydSteinberg', 1, MetodoFloydSteinberg],
                    ['StevensonArce', 3, MetodoStevensonArce],
                    ['Burkes', 2, MetodoBurkes],
                    ['Sierra', 2, MetodoSierra],
                    ['Stucki', 2, MetodoStucki],
                    ['JarvisJudiceNinke', 2, MetodoJarvisJudiceNinke]])

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Trabalho 2 - Aplicacao de meio tons com difusao de erro.')
    parser.add_argument('nomeDoArquivo', help='Nome do arquivo que sera utilizado')
    parser.add_argument('--alternado', help='Use this option if zigzag through the image required.', action='store_true')
    parser.add_argument('--monocromatica', help='Use this option if monochromatic image.', action='store_true')
    args = parser.parse_args()

    imageOriginal = cv2.imread(args.nomeDoArquivo, cv2.IMREAD_COLOR) #Leitura da imagem original

    for x in MASCARAS:
        cv2.imwrite(ArquivoDeSaida(x[0], args.alternado), DifusaoDeErro(imageOriginal, args.alternado, x[1], x[2], 3))

    if args.monocromatica:
        imageOriginal = cv2.imread(args.nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem tons de cinza
        for x in MASCARAS:
            cv2.imwrite(ArquivoDeSaida(x[0] + 'Cinza', args.alternado),
                        DifusaoDeErro(imageOriginal, args.alternado, x[1], x[2], 1))







