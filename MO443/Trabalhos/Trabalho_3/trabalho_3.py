'''
Trabalho - 3
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''

import cv2
import numpy as np
import argparse
from math import exp

def Bernsen(mascara, *desconsiderado):
    return (np.amax(mascara) - np.amin(mascara)) / 2

def Niblack(mascara, pixel, k, *desconsiderado):
    return np.mean(mascara) + k * np.std(mascara)

def SauvolaPietaksinen(mascara, pixel, k, R, *desconsiderado):
    return np.mean(mascara) * ( 1 + k * (np.std(mascara)/R - 1))

def PhansalskarMoreSabale(mascara, pixel, k, R, p, q, ):
    q = q * -1
    return np.mean(mascara) * ( 1 + p * exp(q * np.mean(mascara)) + k * (np.std(mascara)/R - 1))

def Contraste(mascara, pixel, *desconsiderado):
    distanciaDoMinimo = pixel - np.amin(mascara)
    distanciaDoMaximo = abs(pixel - np.amax(mascara))
    if distanciaDoMinimo > distanciaDoMaximo:
        return 255
    else:
        return 0

def Media(mascara, *desconsiderado):
    return np.mean(mascara)

def Mediana(mascara, *desconsiderado):
    return np.median(mascara)

def MetodoGlobal(imagem, limiar):
    return np.where(imagem >= limiar, 0, 255)

def MetodosLocais(imagem, metodo, tamanhoDaMascara, k, R, p, q):
    #imagem = cv2.copyMakeBorder(imagem, tamanhoDaMascara, tamanhoDaMascara, tamanhoDaMascara, tamanhoDaMascara, cv2.BORDER_CONSTANT, value=0)  # aplicação de padding zero com largura do tamanho do pad
    imagemLimiar = np.zeros(imagem.shape)
    deltaXY = tamanhoDaMascara // 2

    for x in range(imagem.shape[0]):
        for y in range(imagem.shape[1]):
            mascara = imagem[max(0, x - deltaXY): min(x + deltaXY + 1, imagem.shape[0]),
                  max(0, y - deltaXY): min(y + deltaXY + 1, imagem.shape[1])]

            imagemLimiar[x, y] = metodo(mascara, imagem[x, y], k, R, p, q)

    imagem = np.where(imagem >= imagemLimiar, 0, 255)
    return imagem

#Nome dos arquivos de saida
def ArquivoDeSaida(nomeDoMetodo):
    return f'outputs/trabalho_3_{nomeDoMetodo}.png'

"""
Constantes
Metodos que irao ser utilizados
"""
METODOS_LOCAIS = np.array([['Bernsen', Bernsen],
                           ['Niblack', Niblack],
                           ['SauvolaPietaksinen', SauvolaPietaksinen],
                           ['PhansalskarMoreSabale', PhansalskarMoreSabale],
                           ['Contraste', Contraste],
                           ['Media', Media],
                           ['Mediana', Mediana]])

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Trabalho 3 - Aplicacao de metodos limiarizacao global e local em imagens monocromaticas.')
    parser.add_argument('nomeDoArquivo', help='Nome do arquivo que sera utilizado')
    parser.add_argument('--limiar', help='Valor de limiar, para ser utilizado na liminiarizacao global, caso nao seja enviado nenhum, o padrao sera 128', default=128, type=int)
    args = parser.parse_args()

    imagemOriginal = cv2.imread(args.nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original
    print(imagemOriginal)
    print(args.limiar)

    cv2.imwrite(ArquivoDeSaida('Global'), MetodoGlobal(np.copy(imagemOriginal), args.limiar))

    for metodo in METODOS_LOCAIS:
        cv2.imwrite(ArquivoDeSaida(metodo[0]), MetodosLocais(np.copy(imagemOriginal), metodo[1], 7, 1,1,1,1))
    #
    # cv2.imwrite(ArquivoDeSaida('Bernsen'), MetodosLocais(np.copy(imagemOriginal), Contraste, 5, 1,1,1,1))







