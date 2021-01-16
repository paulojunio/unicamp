'''
Trabalho - 4 - Decodificador
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''

import cv2
import argparse
import sys

#Escrever o arquivo de saida, com o array de bytes
def EscreverArquivo(arrayDeBytes, arquivo):
    with open(arquivo, "wb") as arquivo: #Escreve arquivo em formato binario
      arquivo.write(bytes([int(arrayDeBytes[i:i + 8], 2) for i in range(0, len(arrayDeBytes), 8)])) #Transforma novamente em 8 em 8 bits para gravar o arquivo

#Metodo para realizar a decodificacao do arquivo
def Decodificador(imagem, plano, arquivoSaida):
    arrayDeBitsTotais = ""
    for x in range(imagem.shape[0]):
        for y in range(imagem.shape[1]):
            r, g, b =  [format(i, "08b") for i in imagem[x][y]]
            arrayDeBitsTotais += r[-1 * plano]
            arrayDeBitsTotais += g[-1 * plano]
            arrayDeBitsTotais += b[-1 * plano]

    arrayDeBits = ""
    for byte in arrayDeBitsTotais:
        arrayDeBits = arrayDeBits + byte
        if arrayDeBits[-100:] == '1111111111111111111111111111111111110000000000000000000000000000011111111111111111111111111111111111': #Encontrado a chave de parada
            break

    EscreverArquivo(arrayDeBits[:-100], f'{arquivoSaida}')

# Metodo principal
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Trabalho 4 - Esteganografia - Decodificador.')
    parser.add_argument('imagemDeSaida', help='Nome da imagem que sera utilizada, deve ser no formato PNG.')
    parser.add_argument('plano_bits', help='Valor do plano de bit que sera utilizado.')
    parser.add_argument('arquivoSaida', help='Nome do arquivo de saida.')
    args = parser.parse_args()

    if int(args.plano_bits) > 2: #Dica para nao usar um plano de bit significativo, porem pode ser utilizado caso o usuario queira
        print('Para melhores resultados use bits menos significativos!')

    imageOriginal = cv2.imread(args.imagemDeSaida, cv2.IMREAD_COLOR)  # Leitura da imagem original

    imagem = Decodificador(imageOriginal, int(args.plano_bits) + 1, args.arquivoSaida)







