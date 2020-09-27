import cv2
import numpy as np
import sys

def PegarPlanoDeBit(imagem, plano):
    imagemDoPlano = np.full((imagemOriginal.shape[0], imagemOriginal.shape[1]), 2 ** int(plano), np.uint8)
    resultado = (cv2.bitwise_and(imagemDoPlano, imagem) * 255) #Multiplicado por 255, para uma melhor visualizacao
    return resultado

nomeDoArquivo, plano = sys.argv[1], sys.argv[2]

imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original
cv2.imshow('Imagem Original', imagemOriginal)

imagemDoPlano = PegarPlanoDeBit(imagemOriginal, plano)
cv2.imshow(f'Plano do bit { plano }', imagemDoPlano)

cv2.waitKey(0)
cv2.destroyAllWindows()