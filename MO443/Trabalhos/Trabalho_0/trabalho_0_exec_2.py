import cv2
import numpy as np
import sys

def ModificarBrilho(imagem, gamma):
    primeiroNumerador = (imagem - imagem.min()).astype('float64')
    primeiroDenominador = (imagem.max() - imagem.min())
    resultado = (primeiroNumerador / primeiroDenominador) ** (1/float(gamma))
    resultado = np.round(resultado * 255).astype(np.uint8)
    return resultado


nomeDoArquivo, gamma = sys.argv[1], sys.argv[2]

imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original
cv2.imshow('Imagem Original', imagemOriginal)

imagemModificada = ModificarBrilho(imagemOriginal, gamma)
cv2.imshow('Imagem modificada', imagemModificada)

cv2.waitKey(0)
cv2.destroyAllWindows()