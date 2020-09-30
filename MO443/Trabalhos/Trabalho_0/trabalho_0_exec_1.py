'''
Trabalho - 0 - Exercicio 1
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''
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
    metadeDeX = int(imagem_x/2)
    if imagem_x % 2 != 0:
        resultado = imagem[0:metadeDeX+1,:]
    else:
        resultado = imagem[0:metadeDeX,:]
    resultado = np.concatenate((resultado, np.flip(imagem[0:metadeDeX:,::-1])))
    return resultado

def ArquivoDeSaida(letra):
    return f'outputs/exercice_1_{letra}.png'

if __name__ == "__main__":

    nomeDoArquivo, letraDoExercicio  = sys.argv[1], sys.argv[2]
    imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original

    if letraDoExercicio.upper() == 'B': #Exercicio B
        negativoDaImagem = ConverteCorNegativo(imagemOriginal)
        cv2.imwrite(ArquivoDeSaida('B'), negativoDaImagem)

    elif letraDoExercicio.upper() == 'C': #Exercicio C
        espalhamentoVertical = EspelharVerticamente(imagemOriginal)
        cv2.imwrite(ArquivoDeSaida('C'), espalhamentoVertical)

    elif letraDoExercicio.upper() == 'D': #Exercicio D
        imagemTransformada = TransformarImagem(imagemOriginal, 100, 200)
        imagemTransformadaOpenCv = TransformarImagemOpenCv(imagemOriginal, 100, 200)
        cv2.imwrite(ArquivoDeSaida('D'), imagemTransformada)
        cv2.imwrite("outputs/exercice_1_D_OpenCV.png", imagemTransformadaOpenCv)

    elif letraDoExercicio.upper() == 'E': #Exercicio E
        linhasInvertidas = InverteLinhas(imagemOriginal)
        cv2.imwrite(ArquivoDeSaida('E'), linhasInvertidas)

    elif letraDoExercicio.upper() == 'F': #Exercicio F
        imagemRefletida = RefletirImagem(imagemOriginal)
        cv2.imwrite(ArquivoDeSaida('F'), imagemRefletida)

    else:
        print("Letra do Exercicio invalida.")
