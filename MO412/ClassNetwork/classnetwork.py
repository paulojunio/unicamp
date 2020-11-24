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

    print(nwx.info(g))
    print(f'Is a bipartite network? {nwx.is_bipartite(g)}')

    return g

def DrawGraph(graph, imageName):

    plt.clf()
    nwx.draw(graph, with_labels=True)
    #plt.show()
    plt.savefig(imageName)

def DrawGraphBipartite(graph, imageName):

    plt.clf()
    # Update position for node from each group
    top = nwx.bipartite.sets(graph)[0]
    pos = nwx.bipartite_layout(graph, top)

    # Draw the network
    nwx.draw(graph, pos=pos, with_labels=True)

    # Plot
    #plt.show()
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
    #plt.show()
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
    #plt.show()
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
    #plt.show()
    plt.savefig(imageName)

def BarGraph(values, nodes, nameOfNodes, imageName):

    plt.clf()
    plt.bar([degree for name, degree in values], [node for node in nodes])
    plt.xlabel("Hobbies")
    plt.ylabel("Degree")
    plt.title(f'Bar graph {nameOfNodes}')
    #plt.show()
    plt.savefig(imageName)

def AllNodesClassNetwork(classNetwork, nameOfNodes):

    print('####################################################')
    if nwx.is_bipartite(classNetwork):
        # Draw the graph using networkx
        DrawGraphBipartite(classNetwork, f'images/DrawGraph{nameOfNodes}')

    else:
        # Draw the graph using networkx
        DrawGraph(classNetwork, f'images/DrawGraph{nameOfNodes}')

    # Plot some scale for the all class network
    PlotNormalScale(classNetwork, f'images/PlotNormal{nameOfNodes}')
    PlotLogLogScale(classNetwork, f'images/PlotLogLog{nameOfNodes}')

    # Plot the histogram for the all class network
    Histogram(classNetwork, classNetwork.nodes(), nameOfNodes, f'images/Histogram{nameOfNodes}')

    # Analyse the components and the giant component
    numberOfComponents = nwx.number_connected_components(classNetwork)
    print(f'Number of components: {numberOfComponents}')

    components = nwx.connected_components(classNetwork)
    sortedComponents = sorted(components, reverse=True)
    giantComponent = classNetwork.subgraph(sortedComponents[0])
    print(f'Size of the giant component in graph {giantComponent.number_of_nodes()}')

    print(
        f'Generate a giantComponent with {giantComponent.number_of_nodes()} nodes, {giantComponent.number_of_edges()} links and average degree is {giantComponent.number_of_edges() * 2 / giantComponent.number_of_nodes()}')

    averageDistance = nwx.average_shortest_path_length(giantComponent)
    print(f'Average distance of giant component is {averageDistance}')

    # Average distance Graph Bipartite
    print(f'Average distance of bipartite graph {nwx.average_shortest_path_length(classNetwork)}')

    # Clustering coefficient, in this case it's 0 for every node
    print(nwx.algorithms.cluster.clustering(classNetwork))



def SeparateNodes(classNetwork, nodes, nameOfNodes):
    # Plot the histogram for the all class network
    Histogram(classNetwork, nodes, nameOfNodes, f'images/Histogram{nameOfNodes}')

    # Graph with all degree
    degreeDistribution = classNetwork.degree(nodes)

    BarGraph(degreeDistribution, nodes, nameOfNodes, f'images/BarGraph{nameOfNodes}')

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
    AllNodesClassNetwork(classNetwork, 'All nodes')

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
    AllNodesClassNetwork(projectionHobbies, 'Projection hobbies')

    # All analysis for projection of students
    AllNodesClassNetwork(projectionStudents, 'Projection students')

    # GenerateGephi file for classNetwork
    GenerateGephi(classNetwork, 'classNetworkGephi')

    # GenerateGephi file for projection hobbies
    GenerateGephi(projectionHobbies, 'hobbiesGephi')

    # GenerateGephi file for projection students
    GenerateGephi(projectionStudents, 'studentsGephi')












