'''
Trabalho - 0 - Exercicio 4
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''
import cv2
import numpy as np
import sys


'''
Criando um mosaico da imagem enviada
Exemplo mosaico

     1  2  3  4              6  8 11 13
     4  5  6  7    ____\     3 16  1  9
     8  9 10 11    ----/    12 14  2  7
    12 13 14 15              4 15 10  5
    
'''

def FazerOMosaico(imagem):
    resultado = np.zeros((imagem.shape))
    imagem_x, imagem_y = imagem.shape

    # As variveis equivalem a seguinte logica xZero e' igual ao primeiro limite do eixo X, xUm e' o segundo limite do eixo X e assim por diante
    xZero, xUm, xDois, xTres = int(imagem_x * 0.25), int(imagem_x * 0.5), int(imagem_x * 0.75), int(imagem_x)
    yZero, yUm, yDois, yTres = int(imagem_y * 0.25), int(imagem_y * 0.5), int(imagem_y * 0.75), int(imagem_y)

    #Primeira linha
    resultado[0:xZero, 0:yZero] = imagem[xZero: xUm, yZero:yUm]
    resultado[0:xZero, yZero:yUm] = imagem[xUm:xDois, yUm:yDois]
    resultado[0:xZero, yUm:yDois] = imagem[xDois:xTres, 0:yZero]
    resultado[0:xZero, yDois:yTres] = imagem[0:xZero, yUm:yDois]
    #Segunda Linha
    resultado[xZero:xUm, 0:yZero] = imagem[xZero:xUm, yDois:yTres]
    resultado[xZero:xUm, yZero:yUm] = imagem[xDois:xTres, yDois:yTres]
    resultado[xZero:xUm, yUm:yDois] = imagem[0:xZero, 0:yZero]
    resultado[xZero:xUm, yDois:yTres] = imagem[xUm:xDois, 0:yZero]
    #Terceira linha
    resultado[xUm:xDois, 0:yZero] = imagem[xUm:xDois, yDois:yTres]
    resultado[xUm:xDois, yZero:yUm] = imagem[xDois:xTres, yZero:yUm]
    resultado[xUm:xDois, yUm:yDois] = imagem[0:xZero, yZero:yUm]
    resultado[xUm:xDois, yDois:yTres] = imagem[xZero:xUm, yUm:yDois]
    #Quarta linha
    resultado[xDois:xTres, 0:yZero] = imagem[0:xZero, yDois:yTres]
    resultado[xDois:xTres, yZero:yUm] = imagem[xDois:xTres, yUm:yDois]
    resultado[xDois:xTres, yUm:yDois] = imagem[xUm:xDois, yZero:yUm]
    resultado[xDois:xTres, yDois:yTres] = imagem[xZero:xUm, 0:yZero]

    return (resultado).astype(np.uint8)


if __name__ == "__main__":

    nomeDoArquivo = sys.argv[1]
    imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original
    imagemModificada = FazerOMosaico(imagemOriginal)
    cv2.imwrite("outputs/exercice_4.png", imagemModificada)
