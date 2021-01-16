'''
Trabalho - 5
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''

import cv2
import numpy as np
import argparse


#Metodos
def Neighbor(imagem, x, y):
    x, y = int(round(x)), int(round(y))
    if x >= imagem.shape[0] or x < 0 or y >= imagem.shape[1] or y < 0:
        return 0

    return imagem[x][y]

#Metodo para calcular a matrix resultante, para que possa ser feita a transformacao
def CalcularMatrix(imagem, angulo, escala, dimensoes):
    #print(imagem.shape) #primeiro valor e' altura e segundo e largura
    matrixResultante = None

    if angulo is not None:
        anguloRad = np.deg2rad(angulo)
        matrixResultante = np.array([[np.cos(anguloRad), -np.sin(anguloRad)],
                                     [np.sin(anguloRad), np.cos(anguloRad)]])
    else:
        altura, largura = imagem.shape[0:2]
        escalaXY = None
        if escala is not None:
            escalaXY = [escala, escala]

        elif dimensoes is not None:
            escalaXY = [dimensoes[0] / largura, dimensoes[1] / altura]
            print(escalaXY)
        else:
            print("Erro, insira os dados corretamente")
            exit()

        matrixResultante = np.array([[escalaXY[1], 0.0], [0.0, escalaXY[0]]])

    return matrixResultante

def TransformarImagem(imagem, matrix, dimensoes, escala, rotacao, metodo):

    matrix = np.linalg.inv(matrix) #Matrix inversa

    if escala is not None and dimensoes is not None:
        dimensoes = (int(dimensoes[0] * escala), int(dimensoes[1] * escala))

    elif escala is not None:
        dimensoes = imagem.shape[0:2]
        dimensoes = (int(dimensoes[1] * escala), int(dimensoes[0] * escala))

    if escala is None and dimensoes is None:
        dimensoes = (imagem.shape[1], imagem.shape[0])

    print(dimensoes)
    imagemDeSaida = np.zeros((dimensoes[1], dimensoes[0]), dtype=np.uint8) #Altura primeiro, altura em segundo

    print(imagemDeSaida.shape)
    for linha in range(0, imagemDeSaida.shape[0]):
        for coluna in range(0, imagemDeSaida.shape[1]):
            if rotacao is None:
                novaCordenada = matrix @ (np.array([[linha], [coluna]]))
            else:
                altura, largura = imagemOriginal.shape
                y_centro = altura // 2
                x_centro = largura // 2
                novaCordenada = matrix @ (np.array([[linha - y_centro], [coluna - x_centro]]))
                novaCordenada[0] = novaCordenada[0] + y_centro
                novaCordenada[1] = novaCordenada[1] + x_centro

            imagemDeSaida[linha][coluna] = metodo(imagem, novaCordenada.ravel()[0], novaCordenada.ravel()[1])

    return imagemDeSaida

"""
Constantes
Metodos para modificar a imagem
"""
METODOS_LOCAIS = np.array([[Neighbor]])

# Metodo principal
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Trabalho 5 - transformacoes geometricas.')
    parser.add_argument('--a', help='Angulo de rotacao medido em graus no sentido anti-horario.', type=float)
    parser.add_argument('--e', help='Fator de escala.', type=float)
    parser.add_argument('--d', help='Dimensao da imagem de saida em pixels. Primeiro largura e depois altura', type=int, nargs=2)
    parser.add_argument('--m', help='Metodo de interpolacao utilizado.', type=int)
    parser.add_argument('nomeDoArquivo', help='Nome do arquivo que sera utilizado, deve ser no formato PNG.')
    parser.add_argument('imagemDeSaida', help='Nome da imagem de saida nop formato png.')
    args = parser.parse_args()

    imagemOriginal = cv2.imread(args.nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original
    if args.m is None:
        print("Precisa escolher um metodo para continuar.")
        exit()

    matrixResultante = CalcularMatrix(np.copy(imagemOriginal), args.a, args.e, args.d)

    imagemModificada = TransformarImagem(imagemOriginal, matrixResultante, args.d, args.e, args.a, METODOS_LOCAIS[int(args.m)][0])

    cv2.imwrite(f'{args.imagemDeSaida}', imagemModificada)




