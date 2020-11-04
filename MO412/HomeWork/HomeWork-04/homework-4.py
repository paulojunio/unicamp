"""
Forth HomeWork
Student: Paulo Junio Reis Rodrigues
"""
import networkx as nwx
import matplotlib.pyplot as plt
import numpy as np

#Plot degree distribution with log log scale
def PlotLogLogScale(degree_freq, label):
    senquence_degrees = range(len(degree_freq))
    plt.title(f"{label} distribution in log log scale")
    plt.loglog(senquence_degrees[0:], degree_freq[0:],'go-')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.show()

def CreateGraph():
    graph = nwx.read_adjlist("net.txt", create_using=nwx.DiGraph())
    print(nwx.info(graph))
    return graph

def OutDegreePlot(graph):
    graphOutDegree = graph.out_degree
    allDegrees = np.asarray([x[1] for x in graphOutDegree])
    degreesOutHist, bin_degrees = np.histogram(allDegrees, bins=allDegrees.max())
    PlotLogLogScale(degreesOutHist / allDegrees.size, "outDegree")

def InDegreePlot(graph):
    graphInDegree = graph.in_degree
    allDegrees = np.asarray([x[1] for x in graphInDegree])
    graphInHist, bin_degrees = np.histogram(allDegrees, bins=allDegrees.max())
    PlotLogLogScale(graphInHist / allDegrees.size, "inDegree")

if __name__ == "__main__":
    graph = CreateGraph()
    OutDegreePlot(graph)
    InDegreePlot(graph)
