'''
Trabalho - 4 - Encoder
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''

import cv2
import numpy as np
import argparse
import sys

#Abrir o arquivo, com o modo binario
def AbrirArquivoBinario(file):
     arquivoBinario = ""
     bytes = bytearray(open(file, "rb").read())
     for i in bytes:
         arquivoBinario = arquivoBinario + str(('{:08b}'.format(i)))
     return arquivoBinario

#Metodo para pegar o arquivo de texto, e transformalo em binario
def GerarArquivoBinario(textoDeEntrada):
    arrayDeBits = AbrirArquivoBinario(textoDeEntrada)

    # Colocando delimitador
    delimitador = '1111111111111111111111111111111111110000000000000000000000000000011111111111111111111111111111111111'

    arrayDeBits = arrayDeBits + delimitador

    return arrayDeBits

#Metodo para realizar a codificacao
def Encoder(imagem, bits, plano):
    numeroDeBytesTotais = imagem.shape[0] * imagem.shape[1] * 3
    print(len(bits), numeroDeBytesTotais)
    if len(bits) > numeroDeBytesTotais: #Verificando se o arquivo pode ser colocando dentro da imagem
        print('Numero de bits nao e permitido')
        sys.exit()

    indexBits = 0
    for x in range(imagem.shape[0]):
        for y in range(imagem.shape[1]):
            r, g, b = [format(i, "08b") for i in imagem[x][y]]
            r, g, b = list(r), list(g), list(b)
            if indexBits < len(bits):
                r[-1 * plano] = bits[indexBits]
                imagem[x][y][0] = int(''.join(r), 2)
                indexBits += 1

            if indexBits < len(bits):
                g[-1 * plano] = bits[indexBits]
                imagem[x][y][1] = int(''.join(g), 2)
                indexBits += 1

            if indexBits < len(bits):
                b[-1 * plano] = bits[indexBits]
                imagem[x][y][2] = int(''.join(b), 2)
                indexBits += 1

            if indexBits >= len(bits):
                break

    return imagem

#Mostrar todos os planos de bits e gravar numa pasta especifica
def MostrarPlano(imagem, plano, args):
    imagemPlano = ((imagem >> plano) % 2) * 255
    for j in range(3):
        cv2.imwrite(f'./planoDeBits/Plano_{plano}_Cor_{j}.png', imagemPlano[:,:,j])

# Metodo principal
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Trabalho 4 - Esteganografia - encode.')
    parser.add_argument('nomeDoArquivo', help='Nome do arquivo que sera utilizado, deve ser no formato PNG.')
    parser.add_argument('arquivoDeEntrada', help='Nome do arquivo texto de entrada.')
    parser.add_argument('plano_bits', help='Valor do plano de bit que sera utilizado.')
    parser.add_argument('imagemDeSaida', help='Nome da imagem de saida.')
    args = parser.parse_args()

    if int(args.plano_bits) > 2:
        print('Para melohores resultados use bits menos significativos!')

    imageOriginal = cv2.imread(args.nomeDoArquivo, cv2.IMREAD_COLOR) #Leitura da imagem original

    arquivoBinario = GerarArquivoBinario(args.arquivoDeEntrada) #Gerando arquivo em uma string binaria

    imagemDeSaida = Encoder(np.copy(imageOriginal), arquivoBinario, int(args.plano_bits) + 1)

    cv2.imwrite(f'{args.imagemDeSaida}', imagemDeSaida)

    for i in range(3):
        MostrarPlano(imagemDeSaida, i, args)

    MostrarPlano(imagemDeSaida, 7, args)





