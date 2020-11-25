'''
Trabalho - 2
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''

import cv2
import numpy as np
import argparse

'''
Esse e' o filtro de Floyd e Steinberg

         | f(x,y) | 7/16
    3/16 |  5/16  | 1/16
    
Invertido

    7/16 | f(x,y) | 
    1/16 |  5/16  | 3/16 
'''
def MetodoFloydSteinberg(imagem, erro, i, j, invertido):
    if not invertido:
        # Propagação do erro normal
        # Primeira linha
        imagem[i][j + 1] = imagem[i][j + 1] + (7 / 16) * erro

        # Segunda linha
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (3 / 16) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (5 / 16) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (1 / 16) * erro

    else:
        # Propagação do erro invertida
        # Primeira linha
        imagem[i][j - 1] = imagem[i][j - 1] + (7 / 16) * erro

        # Segunda linha
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (3 / 16) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (5 / 16) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (1 / 16) * erro

'''
Esse e' o filtro de Stevenson e Arce

       |        |        | f(x,y) |        | 32/200 | 
12/200 |        | 26/200 |        | 30/200 |        | 16/200
       | 12/200 |        | 26/200 |        | 12/200 |
5/200  |        | 12/200 |        | 12/200 |        | 5/200
    
Invertido

       | 32/200 |        | f(x,y) |        |        | 
16/200 |        | 30/200 |        | 26/200 |        | 12/200 
       | 12/200 |        | 26/200 |        | 12/200 |
5/200  |        | 12/200 |        | 12/200 |        | 5/200

'''
def MetodoStevensonArce(imagem, erro, i, j, invertido):
    if not invertido:
        # Propagação do erro normal
        # Primeira linha
        imagem[i][j + 2] = imagem[i][j + 2] + (32 / 200) * erro

        # Segunda linha
        imagem[i + 1][j - 3] = imagem[i + 1][j - 3] + (12 / 200) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (26 / 200) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (30 / 200) * erro
        imagem[i + 1][j + 3] = imagem[i + 1][j + 3] + (16 / 200) * erro

        # Terceira linha
        imagem[i + 2][j - 2] = imagem[i + 2][j - 2] + (12 / 200) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (26 / 200) * erro
        imagem[i + 2][j + 2] = imagem[i + 2][j + 2] + (12 / 200) * erro

        # Quarta linha
        imagem[i + 3][j - 3] = imagem[i + 3][j - 3] + (5 / 200) * erro
        imagem[i + 3][j - 1] = imagem[i + 3][j - 1] + (12 / 200) * erro
        imagem[i + 3][j + 1] = imagem[i + 3][j + 1] + (12 / 200) * erro
        imagem[i + 3][j + 3] = imagem[i + 3][j + 3] + (5 / 200) * erro

    else:

        # Propagação do erro invertido
        # Primeira linha
        imagem[i][j - 2] = imagem[i][j - 2] + (32 / 200) * erro

        # Segunda linha
        imagem[i + 1][j + 3] = imagem[i + 1][j + 3] + (12 / 200) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (26 / 200) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (30 / 200) * erro
        imagem[i + 1][j - 3] = imagem[i + 1][j - 3] + (16 / 200) * erro

        # Terceira linha
        imagem[i + 2][j + 2] = imagem[i + 2][j + 2] + (12 / 200) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (26 / 200) * erro
        imagem[i + 2][j - 2] = imagem[i + 2][j - 2] + (12 / 200) * erro

        # Quarta linha
        imagem[i + 3][j + 3] = imagem[i + 3][j + 3] + (5 / 200) * erro
        imagem[i + 3][j + 1] = imagem[i + 3][j + 1] + (12 / 200) * erro
        imagem[i + 3][j - 1] = imagem[i + 3][j - 1] + (12 / 200) * erro
        imagem[i + 3][j - 3] = imagem[i + 3][j - 3] + (5 / 200) * erro


'''
Esse e' o filtro de Burkes

     |      | f(x,y) | 8/32 | 4/32  
2/32 | 4/32 |  8/32  | 4/32 | 2/32        
       

Invertido

4/32 | 8/32 | f(x,y) |      |  
2/32 | 4/32 |  8/32  | 4/32 | 2/32      

'''

def MetodoBurkes(imagem, erro, i, j, invertido):
    if not invertido:

        # Propagação do erro normal
        # Primeira linha
        imagem[i][j + 1] = imagem[i][j + 1] + (8 / 32) * erro
        imagem[i][j + 2] = imagem[i][j + 2] + (4 / 32) * erro

        # Segunda linha
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (2 / 32) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (4 / 32) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (8 / 32) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (4 / 32) * erro
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (2 / 32) * erro

    else:

        # Propagação do erro invertido
        # Primeira linha
        imagem[i][j - 1] = imagem[i][j - 1] + (8 / 32) * erro
        imagem[i][j - 2] = imagem[i][j - 2] + (4 / 32) * erro

        # Segunda linha
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (2 / 32) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (4 / 32) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (8 / 32) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (4 / 32) * erro
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (2 / 32) * erro


'''
Esse e' o filtro de Sierra

     |      | f(x,y) | 5/32 | 3/32  
2/32 | 4/32 |  5/32  | 4/32 | 2/32    
     | 2/32 |  3/32  | 2/32 |        


Invertido

3/32 | 5/32 | f(x,y) |      |
2/32 | 4/32 |  5/32  | 4/32 | 2/32    
     | 2/32 |  3/32  | 2/32 |        

'''
def MetodoSierra(imagem, erro, i, j, invertido):

    if not invertido:

        # Propagação do erro normal
        # Primeira linha
        imagem[i][j + 1] = imagem[i][j + 1] + (5 / 32) * erro
        imagem[i][j + 2] = imagem[i][j + 2] + (3 / 32) * erro

        # Segunda linha
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (2 / 32) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (4 / 32) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (5 / 32) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (4 / 32) * erro
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (2 / 32) * erro

        # Terceira linha
        imagem[i + 2][j - 1] = imagem[i + 2][j - 1] + (2 / 32) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (3 / 32) * erro
        imagem[i + 2][j + 1] = imagem[i + 2][j + 1] + (2 / 32) * erro

    else:

        # Propagação do erro invertido
        # Primeira linha
        imagem[i][j - 1] = imagem[i][j - 1] + (5 / 32) * erro
        imagem[i][j - 2] = imagem[i][j - 2] + (3 / 32) * erro

        # Segunda linha
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (2 / 32) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (4 / 32) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (5 / 32) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (4 / 32) * erro
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (2 / 32) * erro

        # Terceira linha
        imagem[i + 2][j + 1] = imagem[i + 2][j + 1] + (2 / 32) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (3 / 32) * erro
        imagem[i + 2][j - 1] = imagem[i + 2][j - 1] + (2 / 32) * erro

'''
Esse e' o filtro de Stucki

     |      | f(x,y) | 8/42 | 4/42  
2/42 | 4/42 |  8/42  | 4/42 | 2/42    
1/42 | 2/42 |  4/42  | 2/42 | 1/42  


Invertido

8/42 | 4/42 | f(x,y) |      |
2/42 | 4/42 |  8/42  | 4/42 | 2/42    
1/42 | 2/42 |  4/42  | 2/42 | 1/42     

'''
def MetodoStucki(imagem, erro, i, j, invertido):

    if not invertido:

        # Propagação do erro normal
        # Primeira linha
        imagem[i][j + 1] = imagem[i][j + 1] + (8 / 42) * erro
        imagem[i][j + 2] = imagem[i][j + 2] + (4 / 42) * erro

        # Segunda linha
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (2 / 42) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (4 / 42) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (8 / 42) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (4 / 42) * erro
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (2 / 42) * erro

        # Terceira linha
        imagem[i + 2][j - 2] = imagem[i + 2][j - 2] + (1 / 42) * erro
        imagem[i + 2][j - 1] = imagem[i + 2][j - 1] + (2 / 42) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (4 / 42) * erro
        imagem[i + 2][j + 1] = imagem[i + 2][j + 1] + (2 / 42) * erro
        imagem[i + 2][j + 2] = imagem[i + 2][j + 2] + (1 / 42) * erro

    else:

        # Propagação do erro normal
        # Primeira linha
        imagem[i][j - 1] = imagem[i][j - 1] + (8 / 42) * erro
        imagem[i][j - 2] = imagem[i][j - 2] + (4 / 42) * erro

        # Segunda linha
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (2 / 42) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (4 / 42) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (8 / 42) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (4 / 42) * erro
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (2 / 42) * erro

        # Terceira linha
        imagem[i + 2][j + 2] = imagem[i + 2][j + 2] + (1 / 42) * erro
        imagem[i + 2][j + 1] = imagem[i + 2][j + 1] + (2 / 42) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (4 / 42) * erro
        imagem[i + 2][j - 1] = imagem[i + 2][j - 1] + (2 / 42) * erro
        imagem[i + 2][j - 2] = imagem[i + 2][j - 2] + (1 / 42) * erro

'''
Esse e' o filtro de Jarvis, Judice e Ninke

     |      | f(x,y) | 7/48 | 5/48  
3/48 | 5/48 |  7/48  | 5/48 | 3/48    
1/48 | 3/48 |  5/48  | 3/48 | 1/48 


Invertido

7/48 | 5/48 | f(x,y) |      |
3/48 | 5/48 |  7/48  | 5/48 | 3/48    
1/48 | 3/48 |  5/48  | 3/48 | 1/48    

'''
def MetodoJarvisJudiceNinke(imagem, erro, i, j, invertido):

    if not invertido:

        # Propagação do erro normal
        # Primeira linha
        imagem[i][j + 1] = imagem[i][j + 1] + (7 / 48) * erro
        imagem[i][j + 2] = imagem[i][j + 2] + (5 / 48) * erro

        # Segunda linha
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (3 / 48) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (5 / 48) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (7 / 48) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (5 / 48) * erro
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (3 / 48) * erro

        # Terceira linha
        imagem[i + 2][j - 2] = imagem[i + 2][j - 2] + (1 / 48) * erro
        imagem[i + 2][j - 1] = imagem[i + 2][j - 1] + (3 / 48) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (5 / 48) * erro
        imagem[i + 2][j + 1] = imagem[i + 2][j + 1] + (3 / 48) * erro
        imagem[i + 2][j + 2] = imagem[i + 2][j + 2] + (1 / 48) * erro

    else:

        # Propagação do erro invertido
        # Primeira linha
        imagem[i][j - 1] = imagem[i][j - 1] + (7 / 48) * erro
        imagem[i][j - 2] = imagem[i][j - 2] + (5 / 48) * erro

        # Segunda linha
        imagem[i + 1][j + 2] = imagem[i + 1][j + 2] + (3 / 48) * erro
        imagem[i + 1][j + 1] = imagem[i + 1][j + 1] + (5 / 48) * erro
        imagem[i + 1][j] = imagem[i + 1][j] + (7 / 48) * erro
        imagem[i + 1][j - 1] = imagem[i + 1][j - 1] + (5 / 48) * erro
        imagem[i + 1][j - 2] = imagem[i + 1][j - 2] + (3 / 48) * erro

        # Terceira linha
        imagem[i + 2][j + 2] = imagem[i + 2][j + 2] + (1 / 48) * erro
        imagem[i + 2][j + 1] = imagem[i + 2][j + 1] + (3 / 48) * erro
        imagem[i + 2][j] = imagem[i + 2][j] + (5 / 48) * erro
        imagem[i + 2][j - 1] = imagem[i + 2][j - 1] + (3 / 48) * erro
        imagem[i + 2][j - 2] = imagem[i + 2][j - 2] + (1 / 48) * erro

'''
Metodo que realiza o meio tons por difusao de erro, recebendo como parametro a imagem original,
o valor da flag de alternado, o tamanho do pad da borda que sera criada na imagem, a mascara/filtro que sera usando
para distribuir o erro, e o numero de camadas de cores da imagem
'''
def DifusaoDeErro(imagem, alternado, pad, mascara, camadas):
    imagemOriginal = np.copy(imagem) #Fazendo uma copia da imagem original
    imagemX, imagemY = imagemOriginal.shape[0:2]
    imagemOriginal = cv2.copyMakeBorder(imagemOriginal, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0) # aplicação de padding zero com largura do tamanho do pad
    imagemResultado = np.zeros((imagemX, imagemY, camadas), dtype=np.uint8) # resultado
    imagemOriginal = imagemOriginal.astype(np.float64) #Transformando valores para decimal, para nao haver erro nos calculos
    flag = True

    for i in range(pad, imagemX + pad):
        if flag:
            for j in range(pad, imagemY + pad):
                pixels = np.copy(imagemOriginal[i][j]) # Pegando a copia dos valores dos pixels
                pixels = np.where(pixels < 128, 0, 255) # Atribuindo o valor deles para 0 ou 255, dependendo da condicao valor < 128
                erro = np.subtract(imagemOriginal[i][j], pixels) # Calculando o erro

                mascara(imagemOriginal, erro, i, j, False) #Aplicando a difusao de erro de acordo com a mascara enviada

                imagemResultado[i - pad][j - pad] = pixels
                if alternado:
                    flag = False #Boolean que contra se a varredura sera alternada ou nao
        else:
            for j in range(imagemY-1+pad, pad, -1):
                pixels = np.copy(imagemOriginal[i][j])
                pixels = np.where(pixels < 128, 0, 255)
                erro = np.subtract(imagemOriginal[i][j], pixels)

                mascara(imagemOriginal, erro, i, j, True)

                imagemResultado[i - pad][j - pad] = pixels
                flag = True

    return imagemResultado


#Nome dos arquivos de saida
def ArquivoDeSaida(nomeDoMetodo, alternado):
    if alternado:
        return f'outputs/trabalho_2_{nomeDoMetodo}_alternado.png'

    return f'outputs/trabalho_2_{nomeDoMetodo}.png'


#Constantes - Mascaras para utilizar

'''
Nome do filtro, tamanho do padding, metodo do filtro
'''
MASCARAS = np.array([['FloydSteinberg', 1, MetodoFloydSteinberg],
                    ['StevensonArce', 3, MetodoStevensonArce],
                    ['Burkes', 2, MetodoBurkes],
                    ['Sierra', 2, MetodoSierra],
                    ['Stucki', 2, MetodoStucki],
                    ['JarvisJudiceNinke', 2, MetodoJarvisJudiceNinke]])

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Trabalho 2 - Aplicacao de meio tons com difusao de erro.')
    parser.add_argument('nomeDoArquivo', help='Nome do arquivo que sera utilizado')
    parser.add_argument('--alternado', help='Ao chama-lo a varredura sera feita de forma alternada.', action='store_true')
    parser.add_argument('--monocromatico', help='Ao chama-lo a resposta tambem sera enviada como monocromatica.', action='store_true')
    args = parser.parse_args()

    imageOriginal = cv2.imread(args.nomeDoArquivo, cv2.IMREAD_COLOR) #Leitura da imagem original

    for x in MASCARAS:
        cv2.imwrite(ArquivoDeSaida(x[0], args.alternado), DifusaoDeErro(imageOriginal, args.alternado, x[1], x[2], 3))

    if args.monocromatico:
        imageOriginal = cv2.imread(args.nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original em escala de cinza

        for x in MASCARAS:
            cv2.imwrite(ArquivoDeSaida(x[0] + 'Cinza', args.alternado),
                        DifusaoDeErro(imageOriginal, args.alternado, x[1], x[2], 1))







