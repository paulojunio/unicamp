import cv2
import numpy as np
import sys

def CombinarImagens(primeiraImagem, segundaImagem, escalaUm, escalaDois):
    resultado = cv2.addWeighted(primeiraImagem, 0.7, segundaImagem, 0.3, 0)
    return resultado


primeiroArquivo, escalaUm, segundoArquivo, escalaDois  = sys.argv[1], float(sys.argv[2]), sys.argv[3], float(sys.argv[4])

primeiraImagem = np.array(cv2.imread(primeiroArquivo, cv2.IMREAD_GRAYSCALE)) #Leitura da imagem original
segundaImagem = np.array(cv2.imread(segundoArquivo, cv2.IMREAD_GRAYSCALE)) #Leitura da imagem original

combinacaoDeImagens = CombinarImagens(primeiroArquivo, segundoArquivo, escalaUm, escalaDois)
cv2.imshow(f'Imagens combinadas usando escala {escalaUm } para primeira, e escala {escalaDois} para segunda', combinacaoDeImagens)