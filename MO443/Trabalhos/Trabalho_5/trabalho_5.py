'''
Trabalho - 5
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''

import cv2
import numpy as np
import argparse
import math

#Metodo de polinomios de Lagrange
def PolinomiosLagrange(imagem, x, y):
    resultado = 0
    dx = x - math.floor(x)
    dy = y - math.floor(y)
    ls = np.zeros(5)
    for n in range(1, 5):
        ls[n] += (-dx * (dx - 1) * (dx - 2) * ChecarBorda(imagem, x - 1, y + n - 2))/6
        ls[n] += ((dx + 1) * (dx - 1) * (dx - 2) * ChecarBorda(imagem, x, y + n - 2))/2
        ls[n] += (-dx * (dx + 1) * (dx - 2) * ChecarBorda(imagem, x + 1, y + n - 2))/2
        ls[n] += (dx * (dx + 1) * (dx - 1) * ChecarBorda(imagem, x + 2, y + n - 2))/6

    resultado += (-dy * (dy - 1) * (dy - 2) * ls[1])/6
    resultado += ((dy + 1) * (dy - 1) * (dy - 2) * ls[2])/2
    resultado += (-dy * (dy + 1) * (dy - 2) * ls[3])/2
    resultado += (dy * (dy + 1) * (dy - 1) * ls[4])/6

    return resultado

#Metodo de P para verificar o valor de T e retorna para a funcao bicubica
def P(t):
    if t > 0:
        return t
    else:
        return 0

#Metodo da funcao Bicubica
def Bicubica(imagem, x, y):
    resultado = 0
    dx = x - math.floor(x)
    dy = y - math.floor(y)
    for m in range(0, 4):
        for n in range(0, 4):
            f = ChecarBorda(imagem, x + (m-1), y + (n-1))
            rUm = (1 / 6) * (pow(P(((m-1) - dx) + 2), 3) - 4 * pow(P(((m-1) - dx) + 1), 3) + 6 * pow(P(((m-1) - dx)), 3) - 4 * pow(P(((m-1) - dx) - 1), 3))
            rDois = (1 / 6) * (pow(P((dy - (n-1)) + 2), 3) - 4 * pow(P((dy - (n-1)) + 1), 3) + 6 * pow(P((dy - (n-1))), 3) - 4 * pow(P((dy - (n-1)) - 1), 3))
            resultado = resultado + (f * rUm * rDois)

    return int(round(resultado))

#Metodo da funcao Bilinear
def Bilinear(imagem, x,y):
    p1 = ChecarBorda(imagem, x, y)
    p2 = ChecarBorda(imagem, x, y + 1)
    p3 = ChecarBorda(imagem, x + 1, y)
    p4 = ChecarBorda(imagem, x + 1, y + 1)

    dx = x - math.floor(x)
    dy = y - math.floor(y)

    resultado = ((1-dx) * (1-dy) * p1) + (dx * (1-dy) * p2) + ((1-dx) * dy * p3) + (dx * dy * p4)

    return resultado

#Metodo da funcao para calculos os vizinhos proximos
def VizinhoProximo(imagem, x, y):
    x, y = int(round(x)), int(round(y))
    if x >= imagem.shape[0] or x < 0 or y >= imagem.shape[1] or y < 0:
        return 0
    return imagem[x][y]

#Metodo que checa se o valor enviado ultrapassa ou nao a imagem, para retorna um valor correto
def ChecarBorda(imagem, x, y):
    x, y = int(round(x)), int(round(y))
    if x >= imagem.shape[0]:
        return 0
    elif x < 0:
        return 0
    elif y >= imagem.shape[1]:
        return 0
    elif y < 0:
        return 0
    else:
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

    imagemDeSaida = np.zeros((dimensoes[1], dimensoes[0]), dtype=np.uint8) #Altura primeiro, altura em segundo

    for linha in range(0, imagemDeSaida.shape[0]):
        for coluna in range(0, imagemDeSaida.shape[1]):
            if rotacao is None:
                novaCordenada = matrix @ (np.array([[linha], [coluna]]))
            else:
                altura, largura = imagem.shape
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
METODOS_LOCAIS = np.array([[VizinhoProximo],
                           [Bilinear],
                           [Bicubica],
                           [PolinomiosLagrange]])

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




