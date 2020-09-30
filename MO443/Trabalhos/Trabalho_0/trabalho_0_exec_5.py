'''
Trabalho - 0 - Exercicio 5
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''
import cv2
import sys

#Combinando duas imagens, utilizando duas escalas para cada imagem
def CombinarImagens(primeiraImagem, segundaImagem, escalaUm, escalaDois):
    resultado = cv2.addWeighted(primeiraImagem, escalaUm, segundaImagem, escalaDois, 0)
    return resultado


if __name__ == "__main__":
    primeiroArquivo, escalaUm, segundoArquivo, escalaDois  = sys.argv[1], float(sys.argv[2]), sys.argv[3], float(sys.argv[4])

    primeiraImagem = cv2.imread(primeiroArquivo) #Leitura da primeira imagem
    segundaImagem = cv2.imread(segundoArquivo) #Leitura da segunda imagem

    combinacaoDeImagens = CombinarImagens(primeiraImagem, segundaImagem, escalaUm, escalaDois)
    cv2.imwrite("outputs/exercice_5.png", combinacaoDeImagens)
