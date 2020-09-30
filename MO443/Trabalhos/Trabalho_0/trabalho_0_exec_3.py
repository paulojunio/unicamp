'''
Trabalho - 0 - Exercicio 3
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''
import cv2
import numpy as np
import sys

#Pegando o plano de bit, de acordo com o plano proposto
def PegarPlanoDeBit(imagem, plano):
    imagemDoPlano = np.full((imagemOriginal.shape[0], imagemOriginal.shape[1]), 2 ** int(plano), np.uint8)
    resultado = (cv2.bitwise_and(imagemDoPlano, imagem) * 255) #Multiplicado por 255, para uma melhor visualizacao
    return resultado

if __name__ == "__main__":
    
    nomeDoArquivo, plano = sys.argv[1], sys.argv[2]
    imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original
    imagemDoPlano = PegarPlanoDeBit(imagemOriginal, plano)
    cv2.imwrite("outputs/exercice_3.png", imagemDoPlano)
