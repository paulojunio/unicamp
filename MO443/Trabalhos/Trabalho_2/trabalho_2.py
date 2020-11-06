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

def FloydESteinberg(imagemOriginal, alternado):
    pad = 1
    imagemX, imagemY, camadas = imagemOriginal.shape
    imagemOriginal = cv2.copyMakeBorder(imagemOriginal, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0) # aplicação de padding zero com largura 1
    imagemResultado = np.zeros((imagemX, imagemY, camadas), dtype=np.uint8)  # resultado
    imagemOriginal = imagemOriginal.astype(np.float32)
    linhaPar = True

    for i in range(pad, imagemX):
        if not  alternado and linhaPar:
            for j in range(pad, imagemY):
                pixels = np.copy(imagemOriginal[i][j])

                # print(f'pixels no começo {pixels}')
                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])

                # print(f'pixels no final {pixels} {type(pixels)}')
                #
                # print(f'AAAA{imagemOriginal[i][j]}')

                erros = np.subtract(imagemOriginal[i][j], pixels)

                # print(f'erros de tudo {erros}')

                # propagação do erro
                imagemOriginal[i][j + 1] = imagemOriginal[i][j + 1] + (7 / 16) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (3 / 16) * erros
                imagemOriginal[i + 1][j] = imagemOriginal[i + 1][j + 1] + (5 / 16) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (1 / 16) * erros

                imagemResultado[i][j] = pixels
                if alternado:
                    linhaPar = False
        else:
           # print(imagemY-pad, pad, -1)
            for j in range(imagemY-pad, 0, -1):
                pixels = np.copy(imagemOriginal[i][j])

                # print(f'pixels no começo {pixels}')
                pixels[0] = gerarValores(pixels[0])
                pixels[1] = gerarValores(pixels[1])
                pixels[2] = gerarValores(pixels[2])

                # print(f'pixels no final {pixels} {type(pixels)}')
                #
                # print(f'AAAA{imagemOriginal[i][j]}')

                erros = np.subtract(imagemOriginal[i][j], pixels)

                # print(f'erros de tudo {erros}')

                # propagação do erro
                imagemOriginal[i][j - 1] = imagemOriginal[i][j - 1] + (7 / 16) * erros
                imagemOriginal[i + 1][j + 1] = imagemOriginal[i + 1][j + 1] + (3 / 16) * erros
                imagemOriginal[i + 1][j] = imagemOriginal[i + 1][j] + (5 / 16) * erros
                imagemOriginal[i + 1][j - 1] = imagemOriginal[i + 1][j - 1] + (1 / 16) * erros

                imagemResultado[i][j] = pixels
                linhaPar = True

    #print(imagemResultado)
    return imagemResultado

#Nome dos arquivos de saida
def ArquivoDeSaida(alternado):
    if alternado:
        return f'outputs/trabalho_2_alternado.png'

    return f'outputs/trabalho_2.png'

if __name__ == "__main__":

    nomeDoArquivo, alternado = sys.argv[1], TrueOuFalse(sys.argv[2])
    imageOriginal = cv2.imread(nomeDoArquivo) #Leitura da imagem original
    cv2.imwrite(ArquivoDeSaida(alternado), FloydESteinberg(imageOriginal, alternado))




