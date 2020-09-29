"""
First HomeWork
Student: Paulo Junio Reis Rodrigues
"""
import networkx as nwx
import matplotlib.pyplot as plt
import numpy as np
import random

def PlotNormalScale(graph):
    degree_freq = np.array(nwx.degree_histogram(graph))
    degree_freq = degree_freq
    degrees = range(len(degree_freq))
    plt.title("Degree distribution normal scale")
    plt.plot(degrees[0:], degree_freq[0:], 'ro-')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.show()

def PlotLogLogScale(graph):
    degree_sequence = sorted([d for n, d in graph.degree()], reverse=True)
    plt.loglog(degree_sequence, "ro-", marker="o")
    plt.title("Degree distribution log log scale")
    plt.ylabel("Degree")
    plt.ylabel('Frequency')
    plt.show()

def CustomProbability(sumKmj, beginDegree):
    q = 4/3
    e = 0.00001
    numerator = beginDegree + e
    denominator = sumKmj
    return (numerator/denominator) * q

def CustomProbabilityWithNewSum(graph, beginDegree, j):
    q = 4/3
    e = 0.00001
    sumKmj = 0
    for i in range(1, j):
        sumKmj += graph.degree[i] + e

    numerator = beginDegree + e
    denominator = sumKmj
    return (numerator/denominator) * q

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

#Every every j interation, do the sum += j.degree + e
def SecondExercise(numberNodes):
    graph = nwx.Graph()
    e = 0.00001

    for i in range (0, numberNodes):
        graph.add_node(i)

    for i in range(0, numberNodes):
        sumKmj = 0
        for j in range(i+1, numberNodes):
            if (j > 1):
                sumKmj += graph.degree[j] + e
                if (random.random() < CustomProbability(sumKmj, graph.degree[i])):
                    graph.add_edge(i, j)

    numberLinks = graph.number_of_edges()
    print(f'SecondExercise - Generate a graph with {numberNodes} nodes, {numberLinks} links and average degree is {numberLinks*2/numberNodes}')
    PlotNormalScale(graph)
    PlotLogLogScale(graph)

# Every every j interation, do the sum ( 1 to j )
def SecondExerciseWithNewSum(numberNodes):
    graph = nwx.Graph()

    for i in range (0, numberNodes):
        graph.add_node(i)

    for i in range(0, numberNodes):
        for j in range(i+1, numberNodes):
            if (j > 1):
                if (random.random() < CustomProbabilityWithNewSum(graph, graph.degree[i], j)):
                    graph.add_edge(i, j)

    numberLinks = graph.number_of_edges()
    print(f'SecondExerciseWithNewSum - Generate a graph with {numberNodes} nodes, {numberLinks} links and average degree is {numberLinks*2/numberNodes}')
    PlotNormalScale(graph)
    PlotLogLogScale(graph)

if __name__ == "__main__":
    numberNodes = 300
    probability = 0.0004
    FirstExercise(numberNodes, probability)
    SecondExercise(numberNodes)
    SecondExerciseWithNewSum(numberNodes)
