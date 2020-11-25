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

def DrawGraph(graph, imageName):

    plt.clf()
    nwx.draw(graph, with_labels=True)
    plt.savefig(imageName)

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
def Histogram(graph, nodes, histogramName, imageName):

    degree_sequence = sorted([d for n, d in graph.degree(nodes)], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    plt.clf()
    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color="b")

    plt.title(f"Degree Histogram {histogramName}")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)
    plt.savefig(imageName)

def BarGraph(values, nodes, nameOfNodes, imageName):

    plt.clf()
    plt.bar([node for node in nodes], [round(float(value), 2) for name, value in values])
    plt.xlabel("Hobbies")
    plt.ylabel("Degree")
    plt.title(f'Bar graph {nameOfNodes}')
    plt.savefig(imageName)

def AnalysisTheNetwork(graph, nameOfNodes):

    graph.name = nameOfNodes
    print('####################################################')
    print(nwx.info(graph))
    if nwx.is_bipartite(graph):
        # Draw the graph using networkx
        DrawGraphBipartite(classNetwork, f'images/DrawGraph{nameOfNodes}')

    else:
        # Draw the graph using networkx
        DrawGraph(graph, f'images/DrawGraph{nameOfNodes}')

    # Plot some scale for the all class network
    PlotNormalScale(graph, f'images/PlotNormal{nameOfNodes}')
    PlotLogLogScale(graph, f'images/PlotLogLog{nameOfNodes}')

    # Plot the histogram for the all class network
    Histogram(graph, classNetwork.nodes(), nameOfNodes, f'images/Histogram{nameOfNodes}')

    # Analyse the components and the giant component
    numberOfComponents = nwx.number_connected_components(graph)
    print(f'Number of components: {numberOfComponents}')

    components = nwx.connected_components(graph)
    sortedComponents = sorted(components, reverse=True)
    giantComponent = graph.subgraph(sortedComponents[0])
    print(f'Size of the giant component in graph {giantComponent.number_of_nodes()}')

    # Average distance Graph Bipartite
    print(f'Average distance of bipartite graph {nwx.average_shortest_path_length(graph)}')

    # Clustering coefficient, in this case it's 0 for every node
    clustering = nwx.algorithms.cluster.clustering(graph)
    BarGraph(np.array(list(clustering.items())), graph, 'Clustering of ' + nameOfNodes, f'images/Clustering{nameOfNodes}')

    print(f'Average Clustering coefficient {nwx.algorithms.cluster.average_clustering(graph)}')


def SeparateNodes(graph, nodes, nameOfNodes):
    # Plot the histogram for the all class network
    Histogram(graph, nodes, nameOfNodes, f'images/Histogram{nameOfNodes}')

    # Graph with all degree
    degreeDistribution = np.array(graph.degree(nodes))

    BarGraph(degreeDistribution, nodes, 'Degree distribution of ' + nameOfNodes, f'images/DegreeDistribution{nameOfNodes}')
    print(f'Average degree of {nameOfNodes} is {(graph.number_of_edges())/ len(nodes)}')


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
    AnalysisTheNetwork(classNetwork, 'All nodes')

    #Pick the nodes of the two parts
    hobbies, students = nwx.bipartite.sets(classNetwork)

    #All analysis for hobbies part
    SeparateNodes(classNetwork, hobbies, 'Hobbies')

    #All analysis for student part
    SeparateNodes(classNetwork, students, 'Students')

    #Generate the projection of hobbies graph
    projectionHobbies = nwx.algorithms.bipartite.projected_graph(classNetwork, hobbies)

    # Generate the projection of students graph
    projectionStudents = nwx.algorithms.bipartite.projected_graph(classNetwork, students)

    # All analysis for projection of hobbies
    AnalysisTheNetwork(projectionHobbies, 'Projection hobbies')

    # All analysis for projection of students
    AnalysisTheNetwork(projectionStudents, 'Projection students')

    # GenerateGephi file for classNetwork
    GenerateGephi(classNetwork, 'classNetworkGephi')

    # GenerateGephi file for projection hobbies
    GenerateGephi(projectionHobbies, 'hobbiesGephi')

    # GenerateGephi file for projection students
    GenerateGephi(projectionStudents, 'studentsGephi')












