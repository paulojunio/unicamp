"""
Forth HomeWork
Student: Paulo Junio Reis Rodrigues
"""
import networkx as nwx
import matplotlib.pyplot as plt
import numpy as np

#Plot degree distribution with log log scale
def PlotLogLogScale(degree_freq):
    senquence_degrees = range(len(degree_freq))
    plt.title("Degree distribution log log scale")
    plt.loglog(senquence_degrees[0:], degree_freq[0:],'go-')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.show()

def CreateGraph():
    graph = nwx.read_adjlist("net.txt", create_using=nwx.DiGraph())
    return graph

def OutDegreePlot(graph):
    graphOutDegree = graph.out_degree
    allDegrees = np.asarray([x[1] for x in graphOutDegree])
    degreesOutHist, bin_degrees = np.histogram(allDegrees, bins=allDegrees.max())
    PlotLogLogScale(degreesOutHist / allDegrees.size)

def InDegreePlot(graph):
    graphInDegree = graph.in_degree
    allDegrees = np.asarray([x[1] for x in graphInDegree])
    graphInDegree, bin_degrees = np.histogram(allDegrees, bins=allDegrees.max())
    PlotLogLogScale(graphInDegree / allDegrees.size)


if __name__ == "__main__":
    graph = CreateGraph()
    OutDegreePlot(graph)
    InDegreePlot(graph)
