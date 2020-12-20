"""
tenth HomeWork
Student: Paulo Junio Reis Rodrigues
"""

import networkx as nwx
import matplotlib.pyplot as plt
import random

def PlotDistribute(pinf):
    plt.plot([f*0.05 for f in range(20)], [pinf[f]/pinf[0] for f in range(20)])
    plt.ylabel(' Pinf[f] / Pinf[0] ')
    plt.show()

def CreateGraph():
    graph = nwx.read_adjlist("netA.txt", create_using=nwx.Graph())
    graph.name = 'Homework-10'
    print(nwx.info(graph))
    return graph

if __name__ == "__main__":
    graph = CreateGraph()
    numberOfNodes = graph.number_of_nodes()
    five_percent = int(numberOfNodes * 0.05)
    pinf = [0] * 20
    pinf[0] = len(max(nwx.connected_components(graph), key=len))/numberOfNodes
    for f in range(19):
      list_all_nodes = list(graph.nodes())
      remove_nodes = random.sample(list_all_nodes, five_percent)
      graph.remove_nodes_from(remove_nodes)
      pinf[f+1] = len(max(nwx.connected_components(graph), key=len))/(numberOfNodes - ((f+1) * five_percent))

    PlotDistribute(pinf)