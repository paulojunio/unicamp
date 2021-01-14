'''
Trabalho - 5
Aluno: Paulo Junio Reis Rodrigues
RA: 265674
'''

import cv2
import numpy as np
import argparse
import sys

def MudarOAngulo(imagem, angulo, tipoDeMetodo):
    return 0

def MudarAEscala(imagem, escala, dimensoes, tipoDeMetodo):
    return 0
# Metodo principal
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Trabalho 5 - transformacoes geometricas.')
    parser.add_argument('--a', help='Angulo de rotacao medido em graus no sentido anti-horario.', type=float)
    parser.add_argument('--e', help='Fator de escala.', type=float)
    parser.add_argument('--d', help='Dimensao da imagem de saida em pixels.', type=int, nargs=2)
    parser.add_argument('--m', help='Metodo de interpolacao utilizado.', type=int)
    parser.add_argument('nomeDoArquivo', help='Nome do arquivo que sera utilizado, deve ser no formato PNG.')
    parser.add_argument('imagemDeSaida', help='Nome da imagem de saida nop formato png.')
    args = parser.parse_args()

    imageOriginal = cv2.imread(args.nomeDoArquivo, cv2.IMREAD_COLOR) #Leitura da imagem original
    if args.m is None:
        print("Precisa escolher um metodo para continuar.")
        exit()

    if args.a is not None:
        #Mudar o angulo da imagem
        MudarOAngulo()

    if args.e is not None and args.d is not None:
        #Mudar a escala da imagem
        MudarAEscala()






