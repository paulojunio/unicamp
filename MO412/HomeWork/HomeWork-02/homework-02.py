"""
Second HomeWork
Student: Paulo Junio Reis Rodrigues
"""
import networkx as nwx
import matplotlib.pyplot as plt
import numpy as np
import random

#Plot degree distribution with normal scale
def PlotNormalScale(graph):
    degree_freq = np.array(nwx.degree_histogram(graph))
    degree_freq = degree_freq / graph.number_of_nodes()
    degrees = range(len(degree_freq))
    plt.title("Degree distribution normal scale")
    plt.plot(degrees[0:], degree_freq[0:], 'ro-')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.show()

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

#Create the network with averege degree = 4
def CreateGraph(numberNodes, probability):
    graph = nwx.Graph()
    for i in range (0, numberNodes):
        graph.add_node(i)

    for i in range(0, numberNodes):
        for j in range(i+1, numberNodes):
            if random.random() < probability:
                graph.add_edge(i, j)

    numberLinks = graph.number_of_edges()
    print(f'Using p = {probability}, generate a graph with {numberNodes} nodes, {numberLinks} links and average degree is {numberLinks*2/numberNodes}')
    PlotNormalScale(graph)
    PlotLogLogScale(graph)
    return graph

#Check some informations about the random graph
def CheckInformations(graph):

    numberOfComponents = nwx.number_connected_components(graph)
    print(f'Number of components: {numberOfComponents}')

    components = nwx.connected_components(graph)
    sortedComponents = sorted(components, reverse=True)
    giantComponent = graph.subgraph(sortedComponents[0])
    print(f'Size of the giant component in graph {giantComponent.number_of_nodes()}')

    print(f'Generate a giantComponent with {giantComponent.number_of_nodes()} nodes, {giantComponent.number_of_edges()} links and average degree is {giantComponent.number_of_edges() * 2 / giantComponent.number_of_nodes()}')

    averageDistance = nwx.average_shortest_path_length(giantComponent)
    print(f'Average distance of giant component is {averageDistance}')

if __name__ == "__main__":
    numberNodes = 10000
    probability = 0.0005
    graph = CreateGraph(numberNodes, probability)
    CheckInformations(graph)
