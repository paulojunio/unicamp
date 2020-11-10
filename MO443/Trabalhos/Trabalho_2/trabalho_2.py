'''
Trabalho - 2
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''

import cv2
import numpy as np
import sys

def TrueOuFalse(arg):
    argumento = str(arg).upper()
    if 'TRUE'.startswith(argumento):
       return True
    elif 'FALSE'.startswith(argumento):
       return False
    else:
       print('Argumento invalido')
       sys.exit()

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

def DifusaoDeErro(imagem, alternado, pad, filtro):
    imagemOriginal = np.copy(imagem)
    imagemX, imagemY, camadas = imagemOriginal.shape
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

                if filtro == 1:
                    MetodoFloydSteinberg(imagemOriginal, erro, i, j, False)
                elif filtro == 2:
                    MetodoStevensonArce(imagemOriginal, erro, i, j, False)
                elif filtro == 3:
                    MetodoBurkes(imagemOriginal, erro, i, j, False)
                elif filtro == 4:
                    MetodoSierra(imagemOriginal, erro, i, j, False)
                elif filtro == 5:
                    MetodoStucki(imagemOriginal, erro, i, j, False)
                elif filtro == 6:
                    MetodoJarvisJudiceNinke(imagemOriginal, erro, i, j, False)

                imagemResultado[i - pad][j - pad] = pixels
                if alternado:
                    flag = False
        else:
            for j in range(imagemY-1+pad, pad, -1):
                pixels = np.copy(imagemOriginal[i][j])
                pixels = np.where(pixels < 128, 0, 255)
                erro = np.subtract(imagemOriginal[i][j], pixels)

                if filtro == 1:
                    MetodoFloydSteinberg(imagemOriginal, erro, i, j, True)
                elif filtro == 2:
                    MetodoStevensonArce(imagemOriginal, erro, i, j, True)
                elif filtro == 3:
                    MetodoBurkes(imagemOriginal, erro, i, j, True)
                elif filtro == 4:
                    MetodoSierra(imagemOriginal, erro, i, j, True)
                elif filtro == 5:
                    MetodoStucki(imagemOriginal, erro, i, j, True)
                elif filtro == 6:
                    MetodoJarvisJudiceNinke(imagemOriginal, erro, i, j, True)

                imagemResultado[i - pad][j - pad] = pixels
                flag = True

    return imagemResultado

def DifusaoDeErroEscalaDeCinza(imagem, alternado, pad, filtro):
    imagemOriginal = np.copy(imagem)
    imagemX, imagemY = imagemOriginal.shape
    imagemOriginal = cv2.copyMakeBorder(imagemOriginal, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0) # aplicação de padding zero com largura do tamanho do pad
    imagemResultado = np.zeros((imagemX, imagemY), dtype=np.uint8) # resultado
    imagemOriginal = imagemOriginal.astype(np.float64)
    flag = True

    for i in range(pad, imagemX + pad):
        if flag:
            for j in range(pad, imagemY + pad):
                pixels = np.copy(imagemOriginal[i][j])
                pixels = np.where(pixels < 128, 0, 255)
                erro = np.subtract(imagemOriginal[i][j], pixels)

                if filtro == 1:
                    MetodoFloydSteinberg(imagemOriginal, erro, i, j, False)
                elif filtro == 2:
                    MetodoStevensonArce(imagemOriginal, erro, i, j, False)
                elif filtro == 3:
                    MetodoBurkes(imagemOriginal, erro, i, j, False)
                elif filtro == 4:
                    MetodoSierra(imagemOriginal, erro, i, j, False)
                elif filtro == 5:
                    MetodoStucki(imagemOriginal, erro, i, j, False)
                elif filtro == 6:
                    MetodoJarvisJudiceNinke(imagemOriginal, erro, i, j, False)

                imagemResultado[i - pad][j - pad] = pixels
                if alternado:
                    flag = False
        else:
            for j in range(imagemY-1+pad, pad, -1):
                pixels = np.copy(imagemOriginal[i][j])
                pixels = np.where(pixels < 128, 0, 255)
                erro = np.subtract(imagemOriginal[i][j], pixels)

                if filtro == 1:
                    MetodoFloydSteinberg(imagemOriginal, erro, i, j, True)
                elif filtro == 2:
                    MetodoStevensonArce(imagemOriginal, erro, i, j, True)
                elif filtro == 3:
                    MetodoBurkes(imagemOriginal, erro, i, j, True)
                elif filtro == 4:
                    MetodoSierra(imagemOriginal, erro, i, j, True)
                elif filtro == 5:
                    MetodoStucki(imagemOriginal, erro, i, j, True)
                elif filtro == 6:
                    MetodoJarvisJudiceNinke(imagemOriginal, erro, i, j, True)

                imagemResultado[i - pad][j - pad] = pixels
                flag = True

    return imagemResultado

#Nome dos arquivos de saida
def ArquivoDeSaida(nomeDoMetodo, alternado):
    if alternado:
        return f'outputs/trabalho_2_{nomeDoMetodo}_alternado.png'

    return f'outputs/trabalho_2_{nomeDoMetodo}.png'

#Nome dos arquivos de saida
def ArquivoDeSaidaCinza(nomeDoMetodo, alternado):
    if alternado:
        return f'outputs/trabalho_2_{nomeDoMetodo}_alternado_cinza.png'

    return f'outputs/trabalho_2_{nomeDoMetodo}_cinza.png'

if __name__ == "__main__":

    nomeDoArquivo, alternado = sys.argv[1], TrueOuFalse(sys.argv[2])
    imageOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_COLOR) #Leitura da imagem original
    cv2.imwrite(ArquivoDeSaida('FloydSteinberg', alternado), DifusaoDeErro(imageOriginal, alternado, 1, 1))
    cv2.imwrite(ArquivoDeSaida('StevensonArce', alternado), DifusaoDeErro(imageOriginal, alternado, 3, 2))
    cv2.imwrite(ArquivoDeSaida('Burkes', alternado), DifusaoDeErro(imageOriginal, alternado, 2, 3))
    cv2.imwrite(ArquivoDeSaida('Sierra', alternado), DifusaoDeErro(imageOriginal, alternado, 2, 4))
    cv2.imwrite(ArquivoDeSaida('Stucki', alternado), DifusaoDeErro(imageOriginal, alternado, 2, 5))
    cv2.imwrite(ArquivoDeSaida('JarvisJudiceNinke', alternado), DifusaoDeErro(imageOriginal, alternado, 2, 6))

    imageOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem tons de cinza

    cv2.imwrite(ArquivoDeSaidaCinza('FloydSteinberg', alternado), DifusaoDeErroEscalaDeCinza(imageOriginal, alternado, 1, 1))
    cv2.imwrite(ArquivoDeSaidaCinza('StevensonArce', alternado), DifusaoDeErroEscalaDeCinza(imageOriginal, alternado, 3, 2))
    cv2.imwrite(ArquivoDeSaidaCinza('Burkes', alternado), DifusaoDeErroEscalaDeCinza(imageOriginal, alternado, 2, 3))
    cv2.imwrite(ArquivoDeSaidaCinza('Sierra', alternado), DifusaoDeErroEscalaDeCinza(imageOriginal, alternado, 2, 4))
    cv2.imwrite(ArquivoDeSaidaCinza('Stucki', alternado), DifusaoDeErroEscalaDeCinza(imageOriginal, alternado, 2, 5))
    cv2.imwrite(ArquivoDeSaidaCinza('JarvisJudiceNinke', alternado), DifusaoDeErroEscalaDeCinza(imageOriginal, alternado, 2, 6))







