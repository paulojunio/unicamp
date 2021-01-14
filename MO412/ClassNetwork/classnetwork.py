"""
Student: Paulo Junio Reis Rodrigues
RA:265674
Class Network Analysis
"""

import pandas as pd
import networkx as nwx
import numpy as np
import matplotlib.pyplot as plt
import collections

def CreateClassNetwork(fileName):

    #Read the csv file
    dataframe = pd.read_csv(fileName, sep='\t')
    #Create a graph
    g = nwx.Graph()
    #Pick all columns names
    constant = dataframe.columns.values[1:]
    #Add the all hobbies
    g.add_nodes_from(dataframe.columns.values[1:])
    # Add the all students
    g.add_nodes_from(dataframe['class'].tolist())
    #Generate the numpy dataframe
    dataframeNumpy = dataframe.to_numpy()

    #Create the links
    for i in dataframeNumpy:
        for j in range(1,i.size):
            if i[j] == 1:
                g.add_edge(i[0],constant[j-1])

    return g

# Draw the graph using the networkx
def DrawGraph(graph, imageName):

    plt.clf()
    nwx.draw(graph, with_labels=True)
    plt.savefig(imageName)

# Draw the bipartite graph using the networkx
def DrawGraphBipartite(graph, imageName):

    plt.clf()
    # Update position for node from each group
    top = nwx.bipartite.sets(graph)[0]
    pos = nwx.bipartite_layout(graph, top)

    # Draw the network
    nwx.draw(graph, pos=pos, with_labels=True)

    # Save image
    plt.savefig(imageName)

#Plot degree distribution with normal scale
def PlotNormalScale(graph, imageName):

    degree_freq = np.array(nwx.degree_histogram(graph))
    degree_freq = degree_freq / graph.number_of_nodes()
    degrees = range(len(degree_freq))
    plt.clf()
    plt.title("Degree distribution normal scale")
    plt.plot(degrees[0:], degree_freq[0:], 'ro-')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.savefig(imageName)

#Plot degree distribution with log log scale
def PlotLogLogScale(graph, imageName):

    degree_freq = np.array(nwx.degree_histogram(graph))
    degree_freq = degree_freq / graph.number_of_nodes()
    degrees = range(len(degree_freq))
    plt.clf()
    plt.title("Degree distribution log log scale")
    plt.loglog(degrees[0:], degree_freq[0:], 'go-')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.savefig(imageName)

#Plot degree distribution with histogram
def Histogram(graph, nodes, histogramName, imageName, valueX, valueY):

    degree_sequence = sorted([d for n, d in graph.degree(nodes)], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    plt.clf()
    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80)

    plt.title(f"Degree distribution {histogramName}")
    plt.ylabel(valueY)
    plt.xlabel(valueX)
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)
    plt.savefig(imageName)

#Plot a BarGraph for any value in this script
def BarGraph(values, nodes, nameOfNodes, imageName, valueX, valueY):

    plt.clf()
    plt.bar([node for node in nodes], [round(float(value), 2) for name, value in values])
    plt.xlabel(valueX)
    plt.ylabel(valueY)
    plt.title(f'Bar graph {nameOfNodes}')
    plt.savefig(imageName)

#All the analysis of a specific graph
def AnalysisTheNetwork(graph, nameOfNodes, value):

    graph.name = nameOfNodes
    print('####################################################')
    print(nwx.info(graph))
    if nwx.is_bipartite(graph):
        # Draw the graph using networkx
        DrawGraphBipartite(graph, f'images/DrawGraph{nameOfNodes}')

    else:
        # Draw the graph using networkx
        DrawGraph(graph, f'images/DrawGraph{nameOfNodes}')

    # Plot some scale for the graph
    PlotNormalScale(graph, f'images/PlotNormal{nameOfNodes}')
    PlotLogLogScale(graph, f'images/PlotLogLog{nameOfNodes}')

    # Plot the histogram for the graph
    Histogram(graph, graph.nodes(), nameOfNodes, f'images/Histogram{nameOfNodes}', 'Degree', 'Count')

    # Analyse the components and the giant component
    numberOfComponents = nwx.number_connected_components(graph)
    print(f'Number of components: {numberOfComponents}')

    components = nwx.connected_components(graph)
    sortedComponents = sorted(components, reverse=True)
    giantComponent = graph.subgraph(sortedComponents[0])
    print(f'Size of the giant component in graph {giantComponent.number_of_nodes()}')

    # Average distance graph
    print(f'Average distance of graph {nwx.average_shortest_path_length(graph)}')

    # Clustering coefficient for the graph
    clustering = nwx.algorithms.cluster.clustering(graph)
    BarGraph(np.array(list(clustering.items())), graph, 'Clustering of ' + nameOfNodes, f'images/Clustering{nameOfNodes}', value, 'Clustering coefficient')

    # Average clustering coefficient for the graph
    print(f'Average Clustering coefficient {nwx.algorithms.cluster.average_clustering(graph)}')

# Separate Nodes analysis
def SeparateNodes(graph, nodes, nameOfNodes):
    # Plot the histogram for the all class network
    Histogram(graph, nodes, nameOfNodes, f'images/Histogram{nameOfNodes}', nameOfNodes, 'Degree')

    # Graph with all degree
    degreeDistribution = np.array(graph.degree(nodes))

    BarGraph(degreeDistribution, nodes, 'Degrees of ' + nameOfNodes, f'images/DegreeDistribution{nameOfNodes}', nameOfNodes, 'Degree')
    print(f'Average degree of {nameOfNodes} is {(graph.number_of_edges())/ len(nodes)}')

# Generate the gephi file
def GenerateGephi(graph, fileName):

    f = open(f"{fileName}.net", 'w+')

    f.write(f"*Vertices {graph.number_of_nodes()} \n")
    count = 1
    nodes = np.array(graph.nodes())
    for i in nodes:
        f.write(f'{count} \"{i}\"\n')
        count += 1

    f.write("*Edges \n")
    for i in np.array(graph.edges()):
        firstNode = np.where(nodes == i[0])
        secondNode = np.where(nodes == i[1])
        f.write(f'{firstNode[0][0] + 1} {secondNode[0][0] + 1}\n')

    f.close()

if __name__ == '__main__':

    #Create the class network
    classNetwork = CreateClassNetwork("class-network.tsv")

    #All analysis for classNetwork graph
    AnalysisTheNetwork(classNetwork, 'All nodes', 'All nodes')

    #Pick the nodes of the two parts
    hobbies, students = nwx.bipartite.sets(classNetwork)

    print('oiiiiii',hobbies)
    #All analysis for hobbies part
    SeparateNodes(classNetwork, hobbies, 'Hobbies')

    #All analysis for student part
    SeparateNodes(classNetwork, students, 'Students')

    #Generate the projection of hobbies graph
    projectionHobbies = nwx.algorithms.bipartite.projected_graph(classNetwork, hobbies)

    # Generate the projection of students graph
    projectionStudents = nwx.algorithms.bipartite.projected_graph(classNetwork, students)

    # All analysis for projection of hobbies
    AnalysisTheNetwork(projectionHobbies, 'Projection hobbies', 'Hobbies')

    # All analysis for projection of students
    AnalysisTheNetwork(projectionStudents, 'Projection students', 'Students')

    # GenerateGephi file for classNetwork
    GenerateGephi(classNetwork, 'classNetworkGephi')

    # GenerateGephi file for projection hobbies
    GenerateGephi(projectionHobbies, 'hobbiesGephi')

    # GenerateGephi file for projection students
    GenerateGephi(projectionStudents, 'studentsGephi')












