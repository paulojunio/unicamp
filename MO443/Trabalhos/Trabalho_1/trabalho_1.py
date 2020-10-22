'''
Trabalho - 1
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''
import cv2
import numpy as np
import sys

#Constantes - Filtros utilizados

#Filtro H1
HUM_ARRAY = np.array([[0, 0, -1, 0, 0],
                      [0, -1, -2, -1, 0],
                      [-1, -2, 16, -2, -1],
                      [0, -1, -2, -1, 0],
                      [0, 0, -1, 0, 0]])

#Filtro H2
HDOIS_ARRAY = np.array([[1/256, 4/256, 6/256, 4/256, 1/256],
                        [4/256, 16/256, 24/256, 16/256, 4/256],
                        [6/256, 24/256, 36/256, 24/256, 6/256],
                        [4/256, 16/256, 24/256, 16/256, 4/256],
                        [1/256, 4/256, 6/256, 4/256, 1/256]])

#Filtro H3
HTRES_ARRAY = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

#Filtro H4
HQUATRO_ARRAY = np.array([[-1, -2, -1],
                          [0, 0, 0],
                          [1, 2, 1]])

#Filtro H5
HCINCO_ARRAY = np.array([[-1, -1, -1],
                         [-1, 8, -1],
                         [-1, -1, -1]])

#Filtro H6
HSEIS_ARRAY = np.array([[1/9, 1/9, 1/9],
                        [1/9, 1/9, 1/9],
                        [1/9, 1/9, 1/9]])

#Filtro H7
HSETE_ARRAY = np.array([[-1, -1, 2],
                        [-1, 2, -1],
                        [2, -1, -1]])

#Filtro H8
HOITO_ARRAY = np.array([[2, -1, -1],
                        [-1, 2, -1],
                        [-1, -1, 2]])

#Filtro H9
HNOVE_ARRAY = np.array([[1/9, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1/9, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1/9, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1/9, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1/9, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1/9, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1/9, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1/9, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1/9]])

#Filtro H10
HDEZ_ARRAY = np.array([[-1/8, -1/8, -1/8, -1/8, -1/8],
                        [-1/8, 2/8, 2/8, 2/8, -1/8],
                        [-1/8, 2/8, 8/8, 2/8, -1/8],
                        [-1/8, 2/8, 2/8, 2/8, -1/8],
                        [-1/8, -1/8, -1/8, -1/8, -1/8]])

#Filtro H11
HONZE_ARRAY = np.array([[-1, -1, 0],
                        [-1, 0, 1],
                        [0, 1, 1]])

#Filtro H12
HDOZE_ARRAY = np.array([[0, 1, 1],
                        [-1, 0, 1],
                        [-1, -1, 0]])

#Filtro H13
HTREZE_ARRAY = np.array([[1, 1, 0],
                        [1, 0, -1],
                        [0, -1, -1]])

#Filtro H14
HQUATORZE_ARRAY = np.array([[0, -1, -1],
                            [1, 0, -1],
                            [1, 1, 0]])

#Nome dos arquivos de saida
def ArquivoDeSaida(filtro):
    return f'outputs/trabalho_1_{filtro}.png'

#Metodo para aplicar o filtro utilizando a funcao de correlacao do OpenCV
def AplicarFiltro(imagem, filtro):
    return cv2.filter2D(imagem, -1, filtro[::-1, ::-1], cv2.BORDER_REPLICATE) #Reflitindo o filtro em 180 graus, para que seja feita a correlacao correta

#Metodo para somar as duas imagens, para isso as imagens devem ser transformada para 16 bits, realizar os calculos sqrt((h3^2) + (h4^2)) para que depois possa voltar a 8 bits
def SomarDuasFiltragens(primeiraImagem, segundaImagem):
    return np.round(np.sqrt((np.power(primeiraImagem.astype(np.uint16), 2) + np.power(segundaImagem.astype(np.uint16), 2)))).astype(np.uint8)

if __name__ == "__main__":

    nomeDoArquivo = sys.argv[1]
    imagemOriginal = cv2.imread(nomeDoArquivo, cv2.IMREAD_GRAYSCALE) #Leitura da imagem original

    #Aplicando o filtro h1
    output = AplicarFiltro(imagemOriginal,HUM_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H1'), output)

    # Aplicando o filtro h2
    output = AplicarFiltro(imagemOriginal,HDOIS_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H2'), output)

    # Aplicando o filtro h3
    output_coluna = AplicarFiltro(imagemOriginal,HTRES_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H3'), output_coluna)

    # Aplicando o filtro h4
    output_linha = AplicarFiltro(imagemOriginal, HQUATRO_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H4'), output_linha)

    # Juntando dois filtros, o h3 e o h4
    output = SomarDuasFiltragens(output_coluna, output_linha) #Fazendo o calculo para juntar os filtros, fornecido pelo professor
    cv2.imwrite(ArquivoDeSaida('H3_H4'), output)

    # Aplicando o filtro h5
    output = AplicarFiltro(imagemOriginal,HCINCO_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H5'), output)

    # Aplicando o filtro h6
    output = AplicarFiltro(imagemOriginal, HSEIS_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H6'), output)

    # Aplicando o filtro h7
    output = AplicarFiltro(imagemOriginal,HSETE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H7'), output)

    # Aplicando o filtro h8
    output = AplicarFiltro(imagemOriginal, HOITO_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H8'), output)

    # Aplicando o filtro h9
    output = AplicarFiltro(imagemOriginal, HNOVE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H9'), output)

    # Aplicando o filtro h10
    output = AplicarFiltro(imagemOriginal, HDEZ_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H10'), output)

    # Aplicando o filtro h11
    output = AplicarFiltro(imagemOriginal, HONZE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H11'), output)

    # Aplicando o filtro h12
    output = AplicarFiltro(imagemOriginal, HDOZE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H12'), output)

    # Aplicando o filtro h13
    output = AplicarFiltro(imagemOriginal, HTREZE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H13'), output)

    # Aplicando o filtro h14
    output = AplicarFiltro(imagemOriginal, HQUATORZE_ARRAY)
    cv2.imwrite(ArquivoDeSaida('H14'), output)
