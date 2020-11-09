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

def verificarValores(valores):
    if(valores[0] < 0):
        valores[0] = 0
    if (valores[1] < 0):
        valores[1] = 0
    if (valores[2] < 0):
        valores[2] = 0
    return valores

def gerarValores(pixel):
    if (pixel < 128):
        pixel = 0
    else:
        pixel = 255
    return pixel

def FloydSteinberg(imagemOriginal, alternado, pad):
    imagemX, imagemY, camadas = imagemOriginal.shape
    imagemOriginal = cv2.copyMakeBorder(imagemOriginal, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0) # aplicação de padding zero com largura 1
    imagemResultado = np.zeros((imagemX, imagemY, camadas), dtype=np.uint8)  # resultado
    imagemOriginal = imagemOriginal.astype(np.float32)
    linhaPar = True

    for i in range(pad, imagemX):
        if not alternado and linhaPar:
            for j in range(pad, imagemY):
                pixels = np.copy(imagemOriginal[i][j])

                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])


                erros = np.subtract(imagemOriginal[i][j], pixels)

                # Propagação do erro
                # Primeira linha
                imagemOriginal[i][j + 1] = imagemOriginal[i][j + 1] + (7 / 16) * erros

                # Segunda linha
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (3 / 16) * erros
                imagemOriginal[i + 1][j] = imagemOriginal[i + 1][j + 1] + (5 / 16) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (1 / 16) * erros

                imagemResultado[i][j] = pixels
                if alternado:
                    linhaPar = False
        else:
            for j in range(imagemY-1, 0, -1):
                pixels = np.copy(imagemOriginal[i][j])

                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])


                erros = np.subtract(imagemOriginal[i][j], pixels)

                # Propagação do erro
                # Primeira linha
                imagemOriginal[i][j - 1] = imagemOriginal[i][j - 1] + (7 / 16) * erros

                # Segunda linha
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (3 / 16) * erros
                imagemOriginal[i + 1][j] = imagemOriginal[i + 1][j] + (5 / 16) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (1 / 16) * erros

                imagemResultado[i][j] = pixels
                linhaPar = True

    return imagemResultado


def StevensonArce(imagemOriginal, alternado, pad):
    imagemX, imagemY, camadas = imagemOriginal.shape
    imagemOriginal = cv2.copyMakeBorder(imagemOriginal, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0) # aplicação de padding zero com largura 1
    imagemResultado = np.zeros((imagemX, imagemY, camadas), dtype=np.uint8)  # resultado
    imagemOriginal = imagemOriginal.astype(np.float32)
    linhaPar = True

    for i in range(pad, imagemX):
        if not alternado and linhaPar:
            for j in range(pad, imagemY):
                pixels = np.copy(imagemOriginal[i][j])

                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])

                erros = np.subtract(imagemOriginal[i][j], pixels)

                # Propagação do erro
                # Primeira linha
                imagemOriginal[i][j + 2] = imagemOriginal[i][j + 2] + (32 / 200) * erros

                # Segunda linha
                imagemOriginal[i + 1][j - 3] = imagemOriginal[i + 1][j - 3] + (12 / 200) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (26 / 200) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (30 / 200) * erros
                imagemOriginal[i + 1][j + 3] = imagemOriginal[i + 1][j + 3] + (16 / 200) * erros

                # Terceira linha
                imagemOriginal[i + 2][j - 2] = imagemOriginal[i + 2][j - 2] + (12 / 200) * erros
                imagemOriginal[i + 2][j] = imagemOriginal[i + 2][j] + (26 / 200) * erros
                imagemOriginal[i + 2][j + 2] = imagemOriginal[i + 2][j + 2] + (12 / 200) * erros

                # Quarta linha
                imagemOriginal[i + 1][j - 3] = imagemOriginal[i + 1][j - 3] + (5 / 200) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (12 / 200) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (12 / 200) * erros
                imagemOriginal[i + 1][j + 3] = imagemOriginal[i + 1][j + 3] + (5 / 200) * erros

                imagemResultado[i][j] = pixels
                if alternado:
                    linhaPar = False
        else:
            for j in range(imagemY-1, 0, -1):
                pixels = np.copy(imagemOriginal[i][j])

                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])

                erros = np.subtract(imagemOriginal[i][j], pixels)

                # Propagação do erro
                # Primeira linha
                imagemOriginal[i][j - 2] = imagemOriginal[i][j - 2] + (32 / 200) * erros

                # Segunda linha
                imagemOriginal[i + 1][j + 3] = imagemOriginal[i + 1][j + 3] + (12 / 200) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (26 / 200) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (30 / 200) * erros
                imagemOriginal[i + 1][j - 3] = imagemOriginal[i + 1][j - 3] + (16 / 200) * erros

                # Terceira linha
                imagemOriginal[i + 2][j + 2] = imagemOriginal[i + 2][j + 2] + (12 / 200) * erros
                imagemOriginal[i + 2][j] = imagemOriginal[i + 2][j] + (26 / 200) * erros
                imagemOriginal[i + 2][j - 2] = imagemOriginal[i + 2][j - 2] + (12 / 200) * erros

                # Quarta linha
                imagemOriginal[i + 1][j + 3] = imagemOriginal[i + 1][j + 3] + (5 / 200) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (12 / 200) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (12 / 200) * erros
                imagemOriginal[i + 1][j - 3] = imagemOriginal[i + 1][j - 3] + (5 / 200) * erros

                imagemResultado[i][j] = pixels
                linhaPar = True

    return imagemResultado


def Burkes(imagemOriginal, alternado, pad):
    imagemX, imagemY, camadas = imagemOriginal.shape
    imagemOriginal = cv2.copyMakeBorder(imagemOriginal, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0) # aplicação de padding zero com largura 1
    imagemResultado = np.zeros((imagemX, imagemY, camadas), dtype=np.uint8)  # resultado
    imagemOriginal = imagemOriginal.astype(np.float32)
    linhaPar = True

    for i in range(pad, imagemX):
        if not alternado and linhaPar:
            for j in range(pad, imagemY):
                pixels = np.copy(imagemOriginal[i][j])

                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])


                erros = np.subtract(imagemOriginal[i][j], pixels)

                # Propagação do erro
                # Primeira linha
                imagemOriginal[i][j + 1] = imagemOriginal[i][j + 1] + (8 / 32) * erros
                imagemOriginal[i][j + 2] = imagemOriginal[i][j + 2] + (4 / 32) * erros

                # Segunda linha
                imagemOriginal[i + 1][j - 2] = imagemOriginal[i + 1][j - 2] + (2 / 32) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (4 / 32) * erros
                imagemOriginal[i + 1][j] = imagemOriginal[i + 1][j] + (8 / 32) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (4 / 32) * erros
                imagemOriginal[i + 1][j + 2] = imagemOriginal[i + 1][j + 2] + (2 / 32) * erros

                imagemResultado[i][j] = pixels
                if alternado:
                    linhaPar = False
        else:
            for j in range(imagemY-1, 0, -1):
                pixels = np.copy(imagemOriginal[i][j])

                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])


                erros = np.subtract(imagemOriginal[i][j], pixels)

                # Propagação do erro
                # Primeira linha
                imagemOriginal[i][j - 1] = imagemOriginal[i][j - 1] + (8 / 32) * erros
                imagemOriginal[i][j - 2] = imagemOriginal[i][j - 2] + (4 / 32) * erros

                # Segunda linha
                imagemOriginal[i + 1][j + 2] = imagemOriginal[i + 1][j + 2] + (2 / 32) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (4 / 32) * erros
                imagemOriginal[i + 1][j] = imagemOriginal[i + 1][j] + (8 / 32) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (4 / 32) * erros
                imagemOriginal[i + 1][j - 2] = imagemOriginal[i + 1][j - 2] + (2 / 32) * erros

                imagemResultado[i][j] = pixels
                linhaPar = True

    return imagemResultado


def Sierra(imagemOriginal, alternado, pad):
    imagemX, imagemY, camadas = imagemOriginal.shape
    imagemOriginal = cv2.copyMakeBorder(imagemOriginal, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0) # aplicação de padding zero com largura 1
    imagemResultado = np.zeros((imagemX, imagemY, camadas), dtype=np.uint8)  # resultado
    imagemOriginal = imagemOriginal.astype(np.float32)
    linhaPar = True

    for i in range(pad, imagemX):
        if not alternado and linhaPar:
            for j in range(pad, imagemY):
                pixels = np.copy(imagemOriginal[i][j])

                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])


                erros = np.subtract(imagemOriginal[i][j], pixels)

                # Propagação do erro
                # Primeira linha
                imagemOriginal[i][j + 1] = imagemOriginal[i][j + 1] + (5 / 32) * erros
                imagemOriginal[i][j + 2] = imagemOriginal[i][j + 2] + (3 / 32) * erros

                # Segunda linha
                imagemOriginal[i + 1][j - 2] = imagemOriginal[i + 1][j - 2] + (2 / 32) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (4 / 32) * erros
                imagemOriginal[i + 1][j] = imagemOriginal[i + 1][j] + (5 / 32) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (4 / 32) * erros
                imagemOriginal[i + 1][j + 2] = imagemOriginal[i + 1][j + 2] + (2 / 32) * erros

                # Terceira linha
                imagemOriginal[i + 2][j - 1] = imagemOriginal[i + 2][j - 1] + (2 / 32) * erros
                imagemOriginal[i + 2][j] = imagemOriginal[i + 2][j] + (3 / 32) * erros
                imagemOriginal[i + 2][j + 1] = imagemOriginal[i + 2][j + 1] + (2 / 32) * erros

                imagemResultado[i][j] = pixels
                if alternado:
                    linhaPar = False
        else:
            for j in range(imagemY-1, 0, -1):
                pixels = np.copy(imagemOriginal[i][j])

                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])


                erros = np.subtract(imagemOriginal[i][j], pixels)

                # Propagação do erro
                # Primeira linha
                imagemOriginal[i][j - 1] = imagemOriginal[i][j - 1] + (5 / 32) * erros
                imagemOriginal[i][j - 2] = imagemOriginal[i][j - 2] + (3 / 32) * erros

                # Segunda linha
                imagemOriginal[i + 1][j + 2] = imagemOriginal[i + 1][j + 2] + (2 / 32) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (4 / 32) * erros
                imagemOriginal[i + 1][j] = imagemOriginal[i + 1][j] + (5 / 32) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (4 / 32) * erros
                imagemOriginal[i + 1][j - 2] = imagemOriginal[i + 1][j - 2] + (2 / 32) * erros

                # Terceira linha
                imagemOriginal[i + 2][j + 1] = imagemOriginal[i + 2][j + 1] + (2 / 32) * erros
                imagemOriginal[i + 2][j] = imagemOriginal[i + 2][j] + (3 / 32) * erros
                imagemOriginal[i + 2][j - 1] = imagemOriginal[i + 2][j - 1] + (2 / 32) * erros

                imagemResultado[i][j] = pixels
                linhaPar = True

    return imagemResultado


def Stucki(imagemOriginal, alternado, pad):
    imagemX, imagemY, camadas = imagemOriginal.shape
    imagemOriginal = cv2.copyMakeBorder(imagemOriginal, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0) # aplicação de padding zero com largura 1
    imagemResultado = np.zeros((imagemX, imagemY, camadas), dtype=np.uint8)  # resultado
    imagemOriginal = imagemOriginal.astype(np.float32)
    linhaPar = True

    for i in range(pad, imagemX):
        if not alternado and linhaPar:
            for j in range(pad, imagemY):
                pixels = np.copy(imagemOriginal[i][j])

                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])


                erros = np.subtract(imagemOriginal[i][j], pixels)

                # Propagação do erro
                # Primeira linha
                imagemOriginal[i][j + 1] = imagemOriginal[i][j + 1] + (8 / 42) * erros
                imagemOriginal[i][j + 2] = imagemOriginal[i][j + 2] + (4 / 42) * erros

                # Segunda linha
                imagemOriginal[i + 1][j - 2] = imagemOriginal[i + 1][j - 2] + (2 / 42) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (4 / 42) * erros
                imagemOriginal[i + 1][j] = imagemOriginal[i + 1][j] + (8 / 42) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (4 / 42) * erros
                imagemOriginal[i + 1][j + 2] = imagemOriginal[i + 1][j + 2] + (2 / 42) * erros

                # Terceira linha
                imagemOriginal[i + 2][j - 2] = imagemOriginal[i + 2][j - 2] + (1 / 42) * erros
                imagemOriginal[i + 2][j - 1] = imagemOriginal[i + 2][j - 1] + (2 / 42) * erros
                imagemOriginal[i + 2][j] = imagemOriginal[i + 2][j] + (4 / 42) * erros
                imagemOriginal[i + 2][j + 1] = imagemOriginal[i + 2][j + 1] + (2 / 42) * erros
                imagemOriginal[i + 2][j + 2] = imagemOriginal[i + 2][j + 2] + (1 / 42) * erros

                imagemResultado[i][j] = pixels
                if alternado:
                    linhaPar = False
        else:
            for j in range(imagemY-1, 0, -1):
                pixels = np.copy(imagemOriginal[i][j])

                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])


                erros = np.subtract(imagemOriginal[i][j], pixels)

                # Propagação do erro
                # Primeira linha
                imagemOriginal[i][j - 1] = imagemOriginal[i][j - 1] + (8 / 42) * erros
                imagemOriginal[i][j - 2] = imagemOriginal[i][j - 2] + (4 / 42) * erros

                # Segunda linha
                imagemOriginal[i + 1][j + 2] = imagemOriginal[i + 1][j + 2] + (2 / 42) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (4 / 42) * erros
                imagemOriginal[i + 1][j] = imagemOriginal[i + 1][j] + (8 / 42) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (4 / 42) * erros
                imagemOriginal[i + 1][j - 2] = imagemOriginal[i + 1][j - 2] + (2 / 42) * erros

                # Terceira linha
                imagemOriginal[i + 2][j + 2] = imagemOriginal[i + 2][j + 2] + (1 / 42) * erros
                imagemOriginal[i + 2][j + 1] = imagemOriginal[i + 2][j + 1] + (2 / 42) * erros
                imagemOriginal[i + 2][j] = imagemOriginal[i + 2][j] + (4 / 42) * erros
                imagemOriginal[i + 2][j - 1] = imagemOriginal[i + 2][j - 1] + (2 / 42) * erros
                imagemOriginal[i + 2][j - 2] = imagemOriginal[i + 2][j - 2] + (1 / 42) * erros

                imagemResultado[i][j] = pixels
                linhaPar = True

    return imagemResultado


def JarvisJudiceNinke(imagemOriginal, alternado, pad):
    imagemX, imagemY, camadas = imagemOriginal.shape
    imagemOriginal = cv2.copyMakeBorder(imagemOriginal, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0) # aplicação de padding zero com largura 1
    imagemResultado = np.zeros((imagemX, imagemY, camadas), dtype=np.uint8)  # resultado
    imagemOriginal = imagemOriginal.astype(np.float32)
    linhaPar = True

    for i in range(pad, imagemX):
        if not alternado and linhaPar:
            for j in range(pad, imagemY):
                pixels = np.copy(imagemOriginal[i][j])

                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])


                erros = np.subtract(imagemOriginal[i][j], pixels)

                # Propagação do erro
                # Primeira linha
                imagemOriginal[i][j + 1] = imagemOriginal[i][j + 1] + (7 / 48) * erros
                imagemOriginal[i][j + 2] = imagemOriginal[i][j + 2] + (5 / 48) * erros

                # Segunda linha
                imagemOriginal[i + 1][j - 2] = imagemOriginal[i + 1][j - 2] + (3 / 48) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (5 / 48) * erros
                imagemOriginal[i + 1][j] = imagemOriginal[i + 1][j] + (7 / 48) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (5 / 48) * erros
                imagemOriginal[i + 1][j + 2] = imagemOriginal[i + 1][j + 2] + (3 / 48) * erros

                # Terceira linha
                imagemOriginal[i + 2][j - 2] = imagemOriginal[i + 2][j - 2] + (1 / 48) * erros
                imagemOriginal[i + 2][j - 1] = imagemOriginal[i + 2][j - 1] + (3 / 48) * erros
                imagemOriginal[i + 2][j] = imagemOriginal[i + 2][j] + (5 / 48) * erros
                imagemOriginal[i + 2][j + 1] = imagemOriginal[i + 2][j + 1] + (3 / 48) * erros
                imagemOriginal[i + 2][j + 2] = imagemOriginal[i + 2][j + 2] + (1 / 48) * erros

                imagemResultado[i][j] = pixels
                if alternado:
                    linhaPar = False
        else:
            for j in range(imagemY-1, 0, -1):
                pixels = np.copy(imagemOriginal[i][j])

                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])


                erros = np.subtract(imagemOriginal[i][j], pixels)

                # Propagação do erro
                # Primeira linha
                imagemOriginal[i][j - 1] = imagemOriginal[i][j - 1] + (7 / 48) * erros
                imagemOriginal[i][j - 2] = imagemOriginal[i][j - 2] + (5 / 48) * erros

                # Segunda linha
                imagemOriginal[i + 1][j + 2] = imagemOriginal[i + 1][j + 2] + (3 / 48) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (5 / 48) * erros
                imagemOriginal[i + 1][j] = imagemOriginal[i + 1][j] + (7 / 48) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (5 / 48) * erros
                imagemOriginal[i + 1][j - 2] = imagemOriginal[i + 1][j - 2] + (3 / 48) * erros

                # Terceira linha
                imagemOriginal[i + 2][j + 2] = imagemOriginal[i + 2][j + 2] + (1 / 48) * erros
                imagemOriginal[i + 2][j + 1] = imagemOriginal[i + 2][j + 1] + (3 / 48) * erros
                imagemOriginal[i + 2][j] = imagemOriginal[i + 2][j] + (5 / 48) * erros
                imagemOriginal[i + 2][j - 1] = imagemOriginal[i + 2][j - 1] + (3 / 48) * erros
                imagemOriginal[i + 2][j - 2] = imagemOriginal[i + 2][j - 2] + (1 / 48) * erros

                imagemResultado[i][j] = pixels
                linhaPar = True

    return imagemResultado

#Nome dos arquivos de saida
def ArquivoDeSaida(nomeDoMetodo, alternado):
    if alternado:
        return f'outputs/trabalho_2_{nomeDoMetodo}_alternado.png'

    return f'outputs/trabalho_2_{nomeDoMetodo}.png'

if __name__ == "__main__":

    nomeDoArquivo, alternado = sys.argv[1], TrueOuFalse(sys.argv[2])
    imageOriginal = cv2.imread(nomeDoArquivo) #Leitura da imagem original
    cv2.imwrite(ArquivoDeSaida('FloydSteinberg', alternado), FloydSteinberg(imageOriginal, alternado, 1))
    cv2.imwrite(ArquivoDeSaida('StevensonArce', alternado), StevensonArce(imageOriginal, alternado, 3))
    cv2.imwrite(ArquivoDeSaida('Burkes', alternado), Burkes(imageOriginal, alternado, 2))
    cv2.imwrite(ArquivoDeSaida('Sierra', alternado), Sierra(imageOriginal, alternado, 2))
    cv2.imwrite(ArquivoDeSaida('Stucki', alternado), Stucki(imageOriginal, alternado, 2))
    cv2.imwrite(ArquivoDeSaida('JarvisJudiceNinke', alternado), JarvisJudiceNinke(imageOriginal, alternado, 2))







