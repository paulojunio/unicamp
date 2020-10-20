'''
Trabalho - 0 - Exercicio 1
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''
import cv2
import numpy as np
import sys
from skimage.exposure import rescale_intensity

#Constantes - Filtros utilizados
HUM_ARRAY = np.array([[0, 0, -1, 0, 0],
                      [0, -1, -2, -1, 0],
                      [-1, -2, 16, -2, -1],
                      [0, -1, -2, -1, 0],
                      [0, 0, -1, 0, 0]])

HDOIS_ARRAY = np.array([[1/256, 4/256, 6/256, 4/256, 1/256],
                        [4/256, 16/256, 24/256, 16/256, 4/256],
                        [6/256, 24/256, 36/256, 24/256, 6/256],
                        [4/256, 16/256, 24/256, 16/256, 4/256],
                        [1/256, 4/256, 6/256, 4/256, 1/256]])

HTRES_ARRAY = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

HQUATRO_ARRAY = np.array([[-1, -2, -1],
                          [0, 0, 0],
                          [1, 2, 1]])

HCINCO_ARRAY = np.array([[-1, -1, -1],
                         [-1, 8, -1],
                         [-1, -1, -1]])

HSEIS_ARRAY = np.array([[1/9, 1/9, 1/9],
                        [1/9, 1/9, 1/9],
                        [1/9, 1/9, 1/9]])

HSETE_ARRAY = np.array([[-1, -1, 2],
                        [-1, 2, -1],
                        [2, -1, -1]])

HOITO_ARRAY = np.array([[2, -1, -1],
                        [-1, 2, -1],
                        [-1, -1, 2]])

HNOVE_ARRAY = np.array([[1/9, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1/9, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1/9, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1/9, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1/9, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1/9, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1/9, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1/9, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1/9]])

HDEZ_ARRAY = np.array([[-1/8, -1/8, -1/8, -1/8, -1/8],
                        [-1/8, 2/8, 2/8, 2/8, -1/8],
                        [-1/8, 2/8, 8/8, 2/8, -1/8],
                        [-1/8, 2/8, 2/8, 2/8, -1/8],
                        [-1/8, -1/8, -1/8, -1/8, -1/8]])

HONZE_ARRAY = np.array([[-1, -1, 0],
                        [-1, 0, 1],
                        [0, 1, 1]])

#Normalizacao de uma imagem de acordo com o g_min e o g_max
def TransformarImagem (imagem, g_min, g_max):
    resultado = np.zeros((imagem.shape))
    resultado = cv2.normalize(imagem, resultado, g_min, g_max, cv2.NORM_MINMAX)  # Normalizando via opencv
    return resultado

def convolucao1(imagem, filtro):
    (M, N) = imagem.shape
    (m, n) = filtro.shape
    padn = (n - 1) // 2
    padm = (m - 1) // 2

    imagem = cv2.copyMakeBorder(imagem, padm, padm, padn, padn, cv2.BORDER_DEFAULT)
    imagemSaida = np.zeros((M, N), dtype="float32")

    for y in np.arange(padm, M + padm):
        for x in np.arange(padn, N + padn):
            regiao_da_imagem = imagem[y - padm:y + padm + 1, x - padn:x + padn + 1]
            imagemSaida[y - padm, x - padn] = (regiao_da_imagem * filtro[::-1, ::-1]).sum()

    imagemSaida[imagemSaida <= 0] = 0
    imagemSaida[imagemSaida >= 255] = 255
    imagemSaida = TransformarImagem(imagemSaida, 0, 255).astype("uint8")
    return imagemSaida

def convolucao(imagem, filtro):
    M, N = imagem.shape
    m, n = filtro.shape
    padn, padm = int((n - 1) / 2), int((m - 1) / 2)

    imagem = cv2.copyMakeBorder(imagem, padm, padm, padn, padn, cv2.BORDER_DEFAULT)
    imagemSaida = np.zeros((M, N), dtype="float32")

    for y in np.arange(padm, M + padm):
        for x in np.arange(padn, N + padn):
            regiaoDaImagem = imagem[y - padm:y + padm + 1, x - padn:x + padn + 1]
            imagemSaida[y - padm, x - padn] = (regiaoDaImagem * filtro[::-1, ::-1]).sum()

    imagemSaida = rescale_intensity(imagemSaida, in_range=(0, 255))
    return ( imagemSaida * 255).astype("uint8")

def ArquivoDeSaida(filtro):
    return f'outputs/trabalho_1_{filtro}.png'

def AplicarFiltro(imagem, filtro):
    return cv2.filter2D(imagem, -1, filtro[::-1, ::-1], cv2.BORDER_REPLICATE)

def SomarDuasFiltragens(primeiraImagem, segundaImagem):
    return np.round(np.sqrt((np.power(primeiraImagem.astype(np.uint16), 2) + np.power(segundaImagem.astype(np.uint16), 2)))).astype(np.uint8)

if __name__ == "__main__":

    nomeDoArquivo = sys.argv[1]
    imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original

    #Aplicando o filtro h1
    output = AplicarFiltro(imagemOriginal,HUM_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H1'), output)

    # Aplicando o filtro h2
    output = AplicarFiltro(imagemOriginal,HDOIS_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H2'), output)

    # Aplicando o filtro h3
    output_coluna = AplicarFiltro(imagemOriginal,HTRES_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H3'), output_coluna)

    # Aplicando o filtro h4
    output_linha = AplicarFiltro(imagemOriginal, HQUATRO_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H4'), output_linha)

    # Juntando dois filtros, o h3 e o h4
    output = SomarDuasFiltragens(output_coluna, output_linha) #Fazendo o calculo para juntar os filtros, fornecido pelo professor
    cv2.imwrite(ArquivoDeSaida('H3_H4'), output)

    # Aplicando o filtro h5
    output = AplicarFiltro(imagemOriginal,HCINCO_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H5'), output)

    # Aplicando o filtro h6
    output = AplicarFiltro(imagemOriginal, HSEIS_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H6'), output)

    # Aplicando o filtro h7
    output = AplicarFiltro(imagemOriginal,HSETE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H7'), output)

    # Aplicando o filtro h8
    output = AplicarFiltro(imagemOriginal, HOITO_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H8'), output)

    # Aplicando o filtro h9
    output = AplicarFiltro(imagemOriginal, HNOVE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H9'), output)

    # Aplicando o filtro h10
    output = AplicarFiltro(imagemOriginal, HDEZ_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H10'), output)

    # Aplicando o filtro h11
    output = AplicarFiltro(imagemOriginal, HONZE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H11'), output)




    #==========Outro codigo======Naoentregar
    # output = convolucao(imagemOriginal, HUM_ARRAY)
    # cv2.imwrite(ArquivoDeSaida('MetodoH1'), output)
    #
    # output = convolucao(imagemOriginal, HDOIS_ARRAY)
    # cv2.imwrite(ArquivoDeSaida('MetodoH2'), output)
    #
    # output_coluna = convolucao(imagemOriginal, HTRES_ARRAY)
    # cv2.imwrite(ArquivoDeSaida('MetodoH3'), output_coluna)
    #
    # output_linha = convolucao(imagemOriginal, HQUATRO_ARRAY)
    # cv2.imwrite(ArquivoDeSaida('MetodoH4'), output_linha)
    #
    # output = np.round(
    #     np.sqrt((np.power(output_linha.astype(np.uint16), 2) + np.power(output_coluna.astype(np.uint16), 2)))).astype(
    #     np.uint8)
    # cv2.imwrite(ArquivoDeSaida('MetodoH3_H4'), output)
    #
    # output = convolucao(imagemOriginal, HCINCO_ARRAY)
    # cv2.imwrite(ArquivoDeSaida('MetodoH5'), output)
    #
    # output = convolucao(imagemOriginal, HSEIS_ARRAY)
    # cv2.imwrite(ArquivoDeSaida('MetodoH6'), output)
    #
    # output = convolucao(imagemOriginal, HSETE_ARRAY)
    # cv2.imwrite(ArquivoDeSaida('MetodoH7'), output)
    #
    # output = convolucao(imagemOriginal, HOITO_ARRAY)
    # cv2.imwrite(ArquivoDeSaida('MetodoH8'), output)
    #
    # output = convolucao(imagemOriginal, HNOVE_ARRAY)
    # cv2.imwrite(ArquivoDeSaida('MetodoH9'), output)
    #
    # output = convolucao(imagemOriginal, HDEZ_ARRAY)
    # cv2.imwrite(ArquivoDeSaida('MetodoH10'), output)
    #
    # output = convolucao(imagemOriginal, HONZE_ARRAY)
    # cv2.imwrite(ArquivoDeSaida('MetodoH11'), output)


