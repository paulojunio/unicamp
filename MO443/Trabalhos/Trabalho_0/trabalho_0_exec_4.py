import cv2
import numpy as np
import sys

def FazerOMosaico(imagem):
    resultado = np.zeros((imagem.shape))
    imagem_x, imagem_y = imagem.shape
    xZero, xUm, xDois, xTres = int(imagem_x * 0.25), int(imagem_x * 0.5), int(imagem_x * 0.75), int(imagem_x)
    yZero, yUm, yDois, yTres = int(imagem_y * 0.25), int(imagem_y * 0.5), int(imagem_y * 0.75), int(imagem_y)
    print(int(imagem_x * 0.25), int(imagem_x * 0.5), int(imagem_x * 0.75), int(imagem_x))
    print(int(imagem_y * 0.25), int(imagem_y * 0.5), int(imagem_y * 0.75), int(imagem_y))
    #Primeira linha
    resultado[0:xZero, 0:yZero] = imagem[int(xZero): int(xUm), int(yZero):int(yUm)]
    resultado[0:xZero, yZero:yUm] = imagem[int(xUm):int(xDois), int(yUm):int(yDois)]
    resultado[0:xZero, yUm:yDois] = imagem[int(xDois):int(xTres), 0:int(yZero)]
    resultado[0:xZero, yDois:yTres] = imagem[0:int(xZero), int(yUm):int(yDois)]
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


nomeDoArquivo = sys.argv[1]

imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original
cv2.imshow('Imagem Original', imagemOriginal)

imagemModificada = FazerOMosaico(imagemOriginal)
cv2.imshow('Imagem modificada', imagemModificada)

cv2.waitKey(0)
cv2.destroyAllWindows()