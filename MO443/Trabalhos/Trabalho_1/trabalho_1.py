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

# def convolve(image, kernel):
#     (M, N) = image.shape[:2]
#     (m, n) = kernel.shape[:2]
#     m = int(m // 2)
#     n = int(n // 2)
#     print(m,n)
#
#     for i in np.arange(-1 * m, m + 1):
#         print()
#         for j in np.arange(-1 * n, n + 1):
#             print(kernel[int(i),int(j)], end=" ")
#
#     pad = (n - 1) // 2
#     image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
#     output = np.zeros((M, N), dtype="float32")
#     for y in np.arange(pad, M - 1):
#         for x in np.arange(pad, N - 1):
#             soma = 0
#             for i in np.arange(-1 * m, m + 1):
#                 for j in np.arange(-1 * n, n + 1):
#                     soma += kernel[int(i),int(j)] * image[int(x-i),int(y-j)]
#             output[x,y] = soma
#     output = rescale_intensity(output, in_range=(0, 255))
#     output = (output * 255).astype("uint8")
#     return output

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

if __name__ == "__main__":

    nomeDoArquivo = sys.argv[1]
    imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original

    output = cv2.filter2D(imagemOriginal, -1, HUM_ARRAY[::-1,::-1])
    cv2.imwrite(ArquivoDeSaida('H1'), output)

    output = cv2.filter2D(imagemOriginal, -1, HDOIS_ARRAY[::-1,::-1])
    cv2.imwrite(ArquivoDeSaida('H2'), output)

    output_coluna = cv2.filter2D(imagemOriginal, -1, HTRES_ARRAY[::-1,::-1])
    cv2.imwrite(ArquivoDeSaida('H3'), output_coluna)

    output_linha = cv2.filter2D(imagemOriginal, -1, HQUATRO_ARRAY[::-1,::-1])
    cv2.imwrite(ArquivoDeSaida('H4'), output_linha)

    output = np.round(np.sqrt((np.power(output_linha.astype(np.uint16), 2) + np.power(output_coluna.astype(np.uint16), 2)))).astype(np.uint8)
    cv2.imwrite(ArquivoDeSaida('H3_H4'), output)

    output = cv2.filter2D(imagemOriginal, -1, HCINCO_ARRAY[::-1,::-1])
    cv2.imwrite(ArquivoDeSaida('H5'), output)

    output = cv2.filter2D(imagemOriginal, -1, HSEIS_ARRAY[::-1,::-1])
    cv2.imwrite(ArquivoDeSaida('H6'), output)

    output = cv2.filter2D(imagemOriginal, -1, HSETE_ARRAY[::-1,::-1])
    cv2.imwrite(ArquivoDeSaida('H7'), output)

    output = cv2.filter2D(imagemOriginal, -1, HOITO_ARRAY[::-1,::-1])
    cv2.imwrite(ArquivoDeSaida('H8'), output)

    output = cv2.filter2D(imagemOriginal, -1, HNOVE_ARRAY[::-1,::-1])
    print(output)
    cv2.imwrite(ArquivoDeSaida('H9'), output)

    output = cv2.filter2D(imagemOriginal, -1, HDEZ_ARRAY[::-1,::-1])
    cv2.imwrite(ArquivoDeSaida('H10'), output)

    output = cv2.filter2D(imagemOriginal, -1, HONZE_ARRAY[::-1,::-1])
    cv2.imwrite(ArquivoDeSaida('H11'), output)

    output = convolucao(imagemOriginal, HUM_ARRAY)
    cv2.imwrite(ArquivoDeSaida('MetodoH1'), output)

    output = convolucao(imagemOriginal, HDOIS_ARRAY)
    cv2.imwrite(ArquivoDeSaida('MetodoH2'), output)

    output_coluna = convolucao(imagemOriginal, HTRES_ARRAY)
    cv2.imwrite(ArquivoDeSaida('MetodoH3'), output_coluna)

    output_linha = convolucao(imagemOriginal, HQUATRO_ARRAY)
    cv2.imwrite(ArquivoDeSaida('MetodoH4'), output_linha)

    output = np.round(
        np.sqrt((np.power(output_linha.astype(np.uint16), 2) + np.power(output_coluna.astype(np.uint16), 2)))).astype(
        np.uint8)
    cv2.imwrite(ArquivoDeSaida('MetodoH3_H4'), output)

    output = convolucao(imagemOriginal, HCINCO_ARRAY)
    cv2.imwrite(ArquivoDeSaida('MetodoH5'), output)

    output = convolucao(imagemOriginal, HSEIS_ARRAY)
    cv2.imwrite(ArquivoDeSaida('MetodoH6'), output)

    output = convolucao(imagemOriginal, HSETE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('MetodoH7'), output)

    output = convolucao(imagemOriginal, HOITO_ARRAY)
    cv2.imwrite(ArquivoDeSaida('MetodoH8'), output)

    output = convolucao(imagemOriginal, HNOVE_ARRAY)
    print(output)
    cv2.imwrite(ArquivoDeSaida('MetodoH9'), output)

    output = convolucao(imagemOriginal, HDEZ_ARRAY)
    cv2.imwrite(ArquivoDeSaida('MetodoH10'), output)

    output = convolucao(imagemOriginal, HONZE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('MetodoH11'), output)


