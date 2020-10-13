'''
Trabalho - 0 - Exercicio 1
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''
import cv2
import numpy as np
import sys

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

HDEZ_ARRAY = np.array([[-1, -1, -1, -1, -1],
                        [-1, 2, 2, 2, -1],
                        [-1, 2, 8, 2, -1],
                        [-1, 2, 2, 2, -1],
                        [-1, -1, -1, -1, -1]])

HONZE_ARRAY = np.array([[-1, -1, 0],
                        [-1, 0, 1],
                        [0, 1, 1]])

def ArquivoDeSaida(filtro):
    return f'outputs/trabalho_1_{filtro}.png'

if __name__ == "__main__":

    nomeDoArquivo = sys.argv[1]
    imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original

    output = cv2.filter2D(imagemOriginal, -1, HUM_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H1'), output)

    output = cv2.filter2D(imagemOriginal, -1, HDOIS_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H2'), output)

    output_linha = cv2.filter2D(imagemOriginal, -1, HTRES_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H3'), output_linha)

    output_coluna = cv2.filter2D(imagemOriginal, -1, HQUATRO_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H4'), output_coluna)

    output = np.round(np.sqrt((np.power(output_linha.astype(np.uint16), 2) + np.power(output_coluna.astype(np.uint16), 2)))).astype(np.uint8)
    cv2.imwrite(ArquivoDeSaida('H3_H4'), output)

    output = cv2.filter2D(imagemOriginal, -1, HCINCO_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H5'), output)

    output = cv2.filter2D(imagemOriginal, -1, HSEIS_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H6'), output)

    output = cv2.filter2D(imagemOriginal, -1, HSETE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H7'), output)

    output = cv2.filter2D(imagemOriginal, -1, HOITO_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H8'), output)

    output = cv2.filter2D(imagemOriginal, -1, HNOVE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H9'), output)

    output = cv2.filter2D(imagemOriginal, -1, HDEZ_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H10'), output)

    output = cv2.filter2D(imagemOriginal, -1, HONZE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H11'), output)
