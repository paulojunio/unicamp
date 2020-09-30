'''
Trabalho - 0 - Exercicio 2
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''
import cv2
import numpy as np
import sys

#Modificar um brilho de uma imagem, de acordo com um gamma proposto
def ModificarBrilho(imagem, gamma):
    primeiroNumerador = (imagem - imagem.min()).astype('float64')
    primeiroDenominador = (imagem.max() - imagem.min())
    resultado = (primeiroNumerador / primeiroDenominador) ** (1/float(gamma))
    resultado = np.round(resultado * 255).astype(np.uint8)
    return resultado

if __name__ == "__main__":

    nomeDoArquivo, gamma = sys.argv[1], sys.argv[2]
    imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original
    imagemModificada = ModificarBrilho(imagemOriginal, gamma)
    cv2.imwrite("outputs/exercice_2.png", imagemModificada)

