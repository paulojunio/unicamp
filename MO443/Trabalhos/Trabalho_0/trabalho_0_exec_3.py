'''
Trabalho - 0 - Exercicio 3
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''
import cv2
import numpy as np
import sys

#Normalizacao de uma imagem de acordo com o g_min e o g_max
def NormalizarImagem (imagem, g_min, g_max):
    primeiroNumerador = (imagem - imagem.min()).astype('float64')
    primeiroDenominador = (imagem.max() - imagem.min())
    resultado = np.round(((g_max - g_min) * primeiroNumerador / primeiroDenominador + g_min)).astype(np.uint8) #Aplicando formula de normalizacao, depois arrendando os valores
    return resultado

#Pegando o plano de bit, de acordo com o plano proposto
def PegarPlanoDeBit(imagem, plano):
    imagemDoPlano = np.full((imagemOriginal.shape[0], imagemOriginal.shape[1]), 2 ** int(plano), np.uint8) #Criando uma matriz auxiliar com todos os valores 2 elavado a plano de bit escolhido
    resultado = (cv2.bitwise_and(imagemDoPlano, imagem)) #Multiplicado por 255, para uma melhor visualizacao
    return NormalizarImagem(resultado, 0,255)

if __name__ == "__main__":
    
    nomeDoArquivo, plano = sys.argv[1], int(sys.argv[2])
    if plano < 0 or plano > 7:
        print(f'Plano de bit {plano} invalido')
        sys.exit()

    imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original
    imagemDoPlano = PegarPlanoDeBit(imagemOriginal, plano)
    cv2.imwrite("outputs/exercice_3.png", imagemDoPlano)
