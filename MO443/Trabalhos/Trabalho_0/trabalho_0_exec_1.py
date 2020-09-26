import cv2
import numpy as np
import sys

#Converte uma imagem para tons negativo
def ConverteCorNegativo (imagem):
    resultado = cv2.bitwise_not(imagem)
    return resultado

#Espelhar verticalmente uma imagem 
def EspelharVerticamente (imagem):
    resultado = imagem[::-1]
    return resultado

#Normalizacao de uma imagem de acordo com o g_min e o g_max
def TransformarImagem (imagem, g_min, g_max):
    primeiroNumerador = (imagem - imagem.min()).astype('float64')
    primeiroDenominador = (imagem.max() - imagem.min())
    resultado = np.round(((g_max - g_min) * primeiroNumerador / primeiroDenominador + g_min)).astype(np.uint8)
    return resultado

#Normalizacao de uma imagem (usando OpenCV) de acordo com o g_min e o g_max
def TransformarImagemOpenCv (imagem, g_min, g_max):
    resultado = np.zeros((imagem.shape))
    resultado = cv2.normalize(imagem,  resultado, g_min, g_max, cv2.NORM_MINMAX)
    return resultado

#Inverte as linhas pares da imagem
def InverteLinhas (imagem):
    resultado = np.copy(imagem)
    resultado[0::2,:] = resultado[0::2, ::-1]
    return resultado

#Reflete verticalmente a imagem
def RefletirImagem (imagem):
    imagem_x, imagem_y = imagem.shape
    imagem_x = int(imagem_x/2)
    resultado = imagem[0:imagem_x,:]
    resultado = np.concatenate((resultado, np.flip(imagem[0:imagem_x:,::-1])))
    return resultado


nomeDoArquivo, letraDoExercicio  = sys.argv[1], sys.argv[2]

imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original
cv2.imshow('a) Imagem Original', imagemOriginal)

if letraDoExercicio.upper() == 'B':
    negativoDaImagem = ConverteCorNegativo(imagemOriginal)
    cv2.imshow('b) Negativo da Imagem', negativoDaImagem)
elif letraDoExercicio.upper() == 'C':
    espalhamentoVertical = EspelharVerticamente(imagemOriginal)
    cv2.imshow('c) Espalhamento da Imagem', espalhamentoVertical)

elif letraDoExercicio.upper() == 'D':
    imagemTransformada = TransformarImagem(imagemOriginal, 100, 200)
    imagemTransformadaOpenCv = TransformarImagemOpenCv(imagemOriginal, 100, 200)
    cv2.imshow('d) Imagem transformada', imagemTransformada)
    cv2.imshow('d) Imagem transformada OpenCv', imagemTransformadaOpenCv)

elif letraDoExercicio.upper() == 'E':
    linhasInvertidas = InverteLinhas(imagemOriginal)
    cv2.imshow('e) Linhas pares invertidas', linhasInvertidas)

elif letraDoExercicio.upper() == 'F':
    imagemRefletida = RefletirImagem(imagemOriginal)
    cv2.imshow('f) Reflexao de linhas', imagemRefletida)
else:
    print("Letra do Exercicio invalida.")

cv2.waitKey(0)
cv2.destroyAllWindows()