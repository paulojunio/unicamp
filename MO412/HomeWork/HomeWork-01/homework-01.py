"""
First HomeWork
Student: Paulo Junio Reis Rodrigues
"""
from collections import Counter
from operator import itemgetter
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

#Calculate custom probability
def CustomProbability(sumKmj, beginDegree):
    q = 4/3
    e = 0.00001
    numerator = beginDegree + e
    denominator = sumKmj
    return (numerator/denominator) * q

#Create the network with averege degree = 4
def FirstExercise(numberNodes, probability):
    graph = nwx.Graph()
    for i in range (0, numberNodes):
        graph.add_node(i)

    for i in range(0, numberNodes):
        for j in range(i+1, numberNodes):
            if random.random() < probability:
                graph.add_edge(i, j)

    numberLinks = graph.number_of_edges()
    print(f'FirstExercise- Using p = {probability}, generate a graph with {numberNodes} nodes, {numberLinks} links and average degree is {numberLinks*2/numberNodes}')
    PlotNormalScale(graph)
    PlotLogLogScale(graph)

#Create the network with averege degree = 2.66
def SecondExercise(numberNodes):
    graph = nwx.Graph()

    for i in range(0, numberNodes): #Create graph
        graph.add_node(i)

    for j in range(0, numberNodes):
        sumKmj = 0
        for m in range(1, j): #Do the summation
            sumKmj += graph.degree[m] + 0.00001
        for i in range(1, j):
            if (j > 1):
                if (random.random() < CustomProbability(sumKmj, graph.degree[i])): #Calculate the custom probability
                    graph.add_edge(i, j)

    numberLinks = graph.number_of_edges()
    print(f'SecondExercise - Generate a graph with {numberNodes} nodes, {numberLinks} links and average degree is {numberLinks * 2 / numberNodes}')
    PlotNormalScale(graph)
    PlotLogLogScale(graph)


if __name__ == "__main__":
    numberNodes = 10000
    averegeDegree = 4
    probability = averegeDegree/(numberNodes - 1)# Ad = P * ( N - 1 ) => Ad/(N - 1) = P
    FirstExercise(numberNodes, probability)
    SecondExercise(numberNodes)
