import collections
import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
from networkx.algorithms import bipartite, community

class Algorithms():
  
  def verifyDatabaseInfo(self, dataBase):
    players = dataBase.user_id.unique()
    print("Number of unique players: {}".format(len(players)))

    games = dataBase.game_name.unique() 
    print("Number of unique games: {}".format(len(games)))

  def clusteringCoefficient(self, G):
    """ Compute graph clustering coefficient
    Parameters:
    G- graph to be analysed
    """
    
    cc = nx.average_clustering(G) 
    print("Graph clustering coefficient:", cc)


  def assortativityCoefficient(self, G):
    r = nx.degree_assortativity_coefficient(G)
    print("Degree assortativity coffiecient: ", r)

  def averageDistance(self, G):
    """ Compute graph average distance.
    Since it is a disconnected graph, will be computed
    the average distance for each component
    Parameters:
    G- graph to be analysed
    """
    sub_components = [G.subgraph(c).copy() for c in nx.connected_components(G)]
   
    with open("data/average_shortest_paths.txt", "w") as f:      
      for i, component in enumerate(sub_components):
        print("Component:{}, Number of nodes:{}, Average distance: {}"
          .format(i+1,
            component.number_of_nodes(), 
            nx.average_shortest_path_length(component)), file=f)

  def retrieveLargestComponent(self, G):
    largest_cc = max(nx.connected_components(G), key=len)
    return G.subgraph(largest_cc).copy()
            
  def connectedComponents(self, G, largest_cc):
    """ Compute the number of connected components 
    and size of the giant component
    Parameters:
    -G: graph to be analysed
    """

    ncc = nx.number_connected_components(G)
    print("Number of connected components:", ncc)

     # the size of the giant components
    print("Size of the giant component:", largest_cc.number_of_nodes())


  def degreeCorrelationMatrix(self, G):
    degrees = [y for x,y in G.degree()]
    correlation_matrix = [[0 for i in range(max(degrees)+1)] for j in range(max(degrees)+1)]

    # counting links from degree i to degree j
    for (node_i, node_j) in G.edges:
      correlation_matrix[G.degree(node_i)][G.degree(node_j)] += 1   
      correlation_matrix[G.degree(node_j)][G.degree(node_i)] += 1

    correlation_matrix = correlation_matrix/np.matrix(correlation_matrix).sum()

    sns_plot = sns.heatmap(correlation_matrix, cmap="YlGnBu")
    figure = sns_plot.get_figure()    
    figure.savefig('images/svm_conf.png', dpi=400)
    plt.clf()

  def plotLoglogScale(self, G, imageName):
    """ Plot and save Log Log Scale Graph 
    Parameters:
    -G: graph to be plotted
    -imageName: name to saved image with its extension (.png)
    """
    data = G.degree()
    nodes, nodes_degree  = [n for n, d in data], [d for n, d in data]
    degreeCount = collections.Counter(nodes_degree) 
    accDegree = sorted(degreeCount.items(), key=lambda pair: pair[0], reverse=False) 
    
    degreeSeq = np.zeros(int(max(nodes_degree))+1)

    for x, y in accDegree:
      degreeSeq[x] = y

    degreeSeq = degreeSeq/int(len(nodes))
    plt.loglog(degreeSeq, marker="o")
    plt.title("Degree rank plot")
    plt.ylabel("Probability of degree")
    plt.xlabel("Degree")

    # draw graph in inset
    plt.axes([0.45, 0.45, 0.45, 0.45])
    plt.axis("off")
    fig = plt.gcf()
    #plt.show()
    fig.savefig("images/{}".format(imageName))
    plt.clf()

  def plotNormalScale(self, G, plotTitle, imageName, nodeList):
    """ Plot and save Normal Scale Graph 
    Parameters:
    -G: Graph to be plotted
    -imageName: name to saved image with its extension (.png)
    """
    degree_sequence = sorted([d for n, d in G.degree(nodeList)], reverse=True)  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80)

    plt.title(plotTitle)
    plt.ylabel("Count")
    plt.xlabel("Degree")

    fig = plt.gcf()
    #plt.show()
    fig.savefig("images/{}".format(imageName))
    plt.clf()

  def createProjections(self, G, set1, set2):
    projectionSet1 = bipartite.project(G, set1)
    projectionSet2 = bipartite.project(G, set2)
    return(projectionSet1, projectionSet2)

  def randomFailures(self, G, increments):
    """ 
    Computes and plots the network robustness against random failures.
    To do so, calculate the relative size of the giant component after
    an f fraction of routes randomly removed 
      :param G: Graph to be analysed
      :param increments: f fraction of nodes to be removed
      :type G: Networkx graph
      :type increments: int
    """
    # calculate the relative size of the giant component
    # after an f fraction of routers are randomly removed.
    graph_copy = nx.Graph(G)
    n_nodes = graph_copy.number_of_nodes()
    remove_percent = int(increments * graph_copy.number_of_nodes())
    p_inf = []

    p_inf.append(
      len(max(nx.connected_components(graph_copy), key=len)) / n_nodes
    )

    for i, f in enumerate(np.arange(0.05, 1.0, 0.05)):
      current_nodes = list(graph_copy.nodes())
      nodes_to_remove = random.sample(current_nodes, remove_percent)
      graph_copy.remove_nodes_from(nodes_to_remove)
      p_inf.append(
        len(max(nx.connected_components(graph_copy), key=len))
        / 
          (n_nodes - ((i+1)*remove_percent)) # Normalization [0, 1]
      )

    plt.plot([f for f in np.arange(0, 1.0, 0.05)], [p_inf[f]/p_inf[0] for f in range(20)])
    plt.ylabel('P$\infty$( f ) / P $\infty$(0)')
    plt.xlabel('f', fontsize=15)
    fig = plt.gcf()
    #plt.show()
    fig.savefig('images/p_inf[f]_p_inf[0].png')
    plt.clf()

  def drawNetwork(self, G):
    pos = nx.spring_layout(G, k=0.1)
    nx.draw_networkx(
      G,
      node_size=0, 
      edge_color="#444444", 
      alpha=0.05, 
      with_labels=False)
    plt.savefig('images/plotgraph.png', dpi=400)
    #plt.show()
    plt.clf()

  def identifyCommunities(self, G):
    return (sorted(community.greedy_modularity_communities(G),
      key=len, reverse=True))
    

  def set_node_community(self, G, communities):
    '''Add community to node attributes'''
    for c, v_c in enumerate(communities):
      for v in v_c:
        # Add 1 to save 0 for external edges
        G.nodes[v]['community'] = c + 1

  def set_edge_community(self, G):
    '''Find internal edges and add their community to their attributes'''
    for v, w, in G.edges:
      if G.nodes[v]['community'] == G.nodes[w]['community']:
        # Internal edge, mark with community
        G.edges[v, w]['community'] = G.nodes[v]['community']
      else:
        # External edge, mark as 0
        G.edges[v, w]['community'] = 0


  def get_color(self, i, r_off=1, g_off=1, b_off=1):
    '''Assign a color to a vertex.'''
    r0, g0, b0 = 0, 0, 0
    n = 16
    low, high = 0.1, 0.9
    span = high - low
    r = low + span * (((i + r_off) * 3) % n) / (n - 1)
    g = low + span * (((i + g_off) * 5) % n) / (n - 1)
    b = low + span * (((i + b_off) * 7) % n) / (n - 1)
    return (r, g, b)          

  def plotCommunities(self, G):
    """ Plot communities whithin the graph
    source: https://orbifold.net/default/community-detection-using-networkx/
    acess-date: January, 8th 2021
    """
    auxGraph = G.copy()

    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams.update({'figure.figsize': (15, 10)})
    plt.style.use('dark_background')

    communities = self.identifyCommunities(auxGraph)
    print("Number of communities:", len(communities))

    # Set node and edge communities
    self.set_node_community(auxGraph, communities)
    self.set_edge_community(auxGraph)

    # Set community color for internal edges
    external = [(v, w) for v, w in auxGraph.edges if auxGraph.edges[v, w]['community'] == 0]
    internal = [(v, w) for v, w in auxGraph.edges if auxGraph.edges[v, w]['community'] > 0]
    internal_color = ["black" for e in internal]
    node_color = [self.get_color(auxGraph.nodes[v]['community']) for v in auxGraph.nodes]
    pos = nx.spring_layout(auxGraph, k=0.1)

    # external edges
    nx.draw_networkx(
      auxGraph, 
      pos=pos, 
      node_size=0, 
      edgelist=external, 
      edge_color="silver",
      node_color=node_color,
      alpha=0.2, 
      with_labels=False)

    # internal edges
    nx.draw_networkx(
      auxGraph, 
      pos=pos, 
      edgelist=internal, 
      edge_color=internal_color,
      node_color=node_color,
      alpha=0.05, 
      with_labels=False)

    plt.savefig('images/communities.png', dpi=400)
    plt.clf()
