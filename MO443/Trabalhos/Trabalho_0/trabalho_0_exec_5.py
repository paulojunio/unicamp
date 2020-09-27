import cv2
import sys

def CombinarImagens(primeiraImagem, segundaImagem, escalaUm, escalaDois):
    resultado = cv2.addWeighted(primeiraImagem, escalaUm, segundaImagem, escalaDois, 0)
    return resultado


primeiroArquivo, escalaUm, segundoArquivo, escalaDois  = sys.argv[1], float(sys.argv[2]), sys.argv[3], float(sys.argv[4])

primeiraImagem = cv2.imread(primeiroArquivo) #Leitura da primeira imagem
segundaImagem = cv2.imread(segundoArquivo) #Leitura da segunda imagem

combinacaoDeImagens = CombinarImagens(primeiraImagem, segundaImagem, escalaUm, escalaDois)
cv2.imshow(f'Imagens combinadas usando escala {escalaUm } para primeira, e escala {escalaDois} para segunda', combinacaoDeImagens)

cv2.waitKey(0)
cv2.destroyAllWindows()