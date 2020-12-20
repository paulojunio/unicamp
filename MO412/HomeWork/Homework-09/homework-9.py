"""
Ninth HomeWork
Student: Paulo Junio Reis Rodrigues
"""

import networkx as nwx
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys

def PlotLogLogScale(value_freq):
    plt.title(f"Degree Correlation Function in log log scale")
    plt.scatter(value_freq.keys(), value_freq.values())
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('K')
    plt.ylabel('Knn(K)')
    plt.show()

def CreateGraph():
    graph = nwx.read_adjlist("net8.txt", create_using=nwx.Graph())
    graph.name = 'Homework-9'
    print(nwx.info(graph))
    return graph

def degreeCorrelationMatrix(graph):
    degrees = nwx.degree(graph)
    edges = nwx.edges(graph)
    high_degree = (sorted(graph.degree, key=lambda x: x[1], reverse=True)[0])[1]
    degreeCorrelationMatrix = np.zeros((high_degree+1, high_degree+1))
    for edge in edges:
        degreeCorrelationMatrix[degrees[edge[0]]][degrees[edge[1]]] = degreeCorrelationMatrix[degrees[edge[0]]][degrees[edge[1]]] + 1
        degreeCorrelationMatrix[degrees[edge[1]]][degrees[edge[0]]] = degreeCorrelationMatrix[degrees[edge[1]]][degrees[edge[0]]] + 1

    ax = sns.heatmap(degreeCorrelationMatrix / degreeCorrelationMatrix.sum())
    np.set_printoptions(threshold=sys.maxsize)
    plt.show()

def degreeCorrelationFunction(graph):
    degreeCorrelation = nwx.average_degree_connectivity(graph)
    PlotLogLogScale(degreeCorrelation)

def degreeCorrelationCoefficient(graph):
    r = nwx.degree_pearson_correlation_coefficient(graph)
    print(f'The degree correlation coefficient is {r}')

if __name__ == "__main__":
    graph = CreateGraph()
    degreeCorrelationCoefficient(graph)
    degreeCorrelationMatrix(graph)
    degreeCorrelationFunction(graph)


