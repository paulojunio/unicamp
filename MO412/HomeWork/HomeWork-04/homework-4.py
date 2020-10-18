"""
Forth HomeWork
Student: Paulo Junio Reis Rodrigues
"""
import networkx as nwx
import matplotlib.pyplot as plt
import numpy as np
import random


#Plot degree distribution with log log scale
def PlotLogLogScale(graph):
    degree_freq = np.array(nwx.degree_histogram(graph))
    degree_freq = degree_freq / graph.number_of_nodes()
    degrees = range(len(degree_freq))
    plt.title("Degree distribution log log scale")
    plt.loglog(degrees[0:], degree_freq[0:], 'go-')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.show()

def CreateGraph():
    graph = nwx.DiGraph()

    arquivo_ligacoes = open("net.txt", "r")

    for linha in arquivo_ligacoes:
        valores = linha.split()
        print(valores[0], valores[1])

    ref_arquivo.close()

    return graph

if __name__ == "__main__":
    graph = CreateGraph()
