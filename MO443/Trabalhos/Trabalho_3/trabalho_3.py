'''
Trabalho - 3
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''

import cv2
import numpy as np
import argparse
from math import exp
from matplotlib import pyplot as plt

def GerarHistograma(imagem, nomeDoMetodo):
    plt.clf()
    plt.hist(imagem.ravel(), 256 , [0,256])
    plt.xlabel("Niveis de cinza")
    plt.ylabel("Quantidade de pixels")
    plt.savefig(f'histogramas/histrograma_{nomeDoMetodo}')

def FracaoDePixelsPretos(imagem, nomeDoMetodo):
    print(f"Nome do Metodo {nomeDoMetodo}")
    numPixelsBrancos = np.count_nonzero(imagem)
    numPixelsPretos = imagem.size - numPixelsBrancos
    print("Fracao de pixels pretos: ", numPixelsPretos / imagem.size)
    print("Fracao de pixels brancos: ", numPixelsBrancos / imagem.size)

def Bernsen(mascara, *desconsiderado):
    return (np.amin(mascara) + np.amax(mascara)) / 2

def Niblack(mascara, pixel, k, *desconsiderado):
    return np.mean(mascara) + (k * np.std(mascara))

def SauvolaPietaksinen(mascara, pixel, k, R, *desconsiderado):
    return np.mean(mascara) * (1 + k * ((np.std(mascara)/R) - 1))

def PhansalskarMoreSabale(mascara, pixel, k, R, p, q):
    q = q * -1
    return np.mean(mascara) * (1 + p * exp(q * np.mean(mascara)) + k * ((np.std(mascara)/R) - 1))

def Contraste(mascara, pixel, *desconsiderado):
    distanciaDoMinimo = pixel - np.amin(mascara)
    distanciaDoMaximo = np.amax(mascara) - pixel

    if distanciaDoMinimo > distanciaDoMaximo:
        return 0
    else:
        return 255

def Media(mascara, *desconsiderado):
    return np.mean(mascara)

def Mediana(mascara, *desconsiderado):
    return np.median(mascara)

def MetodoGlobal(imagem, limiar):
    return np.where(imagem > limiar, 0, 255)

def MetodosLocais(imagem, metodo, tamanhoDaMascara, k, R, p, q):
    imagemLimiar = np.zeros(imagem.shape)
    imagemReposta = np.copy(imagem)
    imagem = cv2.copyMakeBorder(imagem, tamanhoDaMascara, tamanhoDaMascara, tamanhoDaMascara, tamanhoDaMascara, cv2.BORDER_REPLICATE) # aplicação de padding igual a borada com largura do tamanho do pad
    deltaXY = tamanhoDaMascara // 2

    for x in range(tamanhoDaMascara, imagem.shape[0] - tamanhoDaMascara):
        for y in range(tamanhoDaMascara, imagem.shape[1] - tamanhoDaMascara):
            mascara = np.copy(imagem[x - deltaXY : x + deltaXY + 1, y - deltaXY : y + deltaXY + 1])
            imagemLimiar[x - tamanhoDaMascara, y - tamanhoDaMascara] = metodo(mascara, imagem[x, y], k, R, p, q) #Valores: Mascara, pixel, k, R, p e q

    imagemReposta = np.uint8(np.where(imagemReposta > imagemLimiar, 0, 255))
    return imagemReposta

#Nome dos arquivos de saida
def ArquivoDeSaida(nomeDoMetodo):
    return f'outputs/trabalho_3_{nomeDoMetodo}.pgm'

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
    parser.add_argument('nomeDoArquivo', help='Nome do arquivo que sera utilizado.')
    parser.add_argument('--limiar', help='Valor de limiar, para ser utilizado na liminiarizacao global, caso nao seja enviado nenhum, o padrao sera 128.', default=128, type=int)
    parser.add_argument('--mascara', help='Tamanho da mascara que sera aplicado nas liminiarizacao local, o padrao sera 3.', default=3, type=int)
    parser.add_argument('--k', help='Valor do parametro k, o padrao sera 0.25.', default=0.25, type=float)
    parser.add_argument('--R', help='Valor do parametro R, o padrao sera 0.5.', default=0.5, type=float)
    parser.add_argument('--p', help='Valor do parametro p, o padrao sera 2.', default=2, type=float)
    parser.add_argument('--q', help='Valor do parametro q, o padrao sera 10.', default=10, type=float)
    args = parser.parse_args()


    imagemOriginal = np.float64(cv2.imread(args.nomeDoArquivo, cv2.IMREAD_GRAYSCALE)) #Leitura da imagem original, e convertendo para float 64 para nao atrapalhar nos calculos
    GerarHistograma(imagemOriginal, 'Original')

    imagemResultado = MetodoGlobal(np.copy(imagemOriginal), args.limiar)
    cv2.imwrite(ArquivoDeSaida('Global'), imagemResultado)
    GerarHistograma(imagemResultado, 'Global')
    FracaoDePixelsPretos(imagemResultado, 'Global')

    for metodo in METODOS_LOCAIS:
        imagemResultado = MetodosLocais(np.copy(imagemOriginal), metodo[1], args.mascara, args.k, args.R, args.p, args.q)
        GerarHistograma(imagemResultado, metodo[0])
        cv2.imwrite(ArquivoDeSaida(metodo[0]), imagemResultado)
        FracaoDePixelsPretos(imagemResultado, metodo[0])







