"""
Forth HomeWork
Student: Paulo Junio Reis Rodrigues
"""
import networkx as nwx
import matplotlib.pyplot as plt
import numpy as np
import random


#Plot degree distribution with log log scale
def PlotLogLogScale(degree_freq):
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
        graph.add_node(valores[0])
        graph.add_node(valores[1])
        graph.add_edge(valores[0], valores[1])

    arquivo_ligacoes.close()
    return graph

def OutDegreePlot(graph):
    graphOutDegree = graph.out_degree
    allDegrees = np.asarray([x[1] for x in graphOutDegree])
    degreesOutFreq = np.zeros(allDegrees.max() + 1, dtype=int)
    for x in allDegrees:
        degreesOutFreq[x] += 1
    print(degreesOutFreq / allDegrees.size)
    PlotLogLogScale(degreesOutFreq / allDegrees.size)

def InDegreePlot(graph):
    graphInDegree = graph.in_degree
    allDegrees = np.asarray([x[1] for x in graphInDegree])
    degreesInFreq = np.zeros(allDegrees.max() + 1, dtype=int)
    for x in allDegrees:
        degreesInFreq[x] += 1
    print(degreesInFreq / allDegrees.size)
    PlotLogLogScale(degreesInFreq / allDegrees.size)


if __name__ == "__main__":
    graph = CreateGraph()
    OutDegreePlot(graph)
    InDegreePlot(graph)
