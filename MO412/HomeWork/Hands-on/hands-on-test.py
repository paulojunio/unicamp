"""
Hands On
Student: Paulo Junio Reis Rodrigues
"""
import sys
import networkx as nwx
import random

def createGraph(numberNodes, probability):
    graph = nwx.Graph()
    for i in range (0, numberNodes):
        graph.add_node(i)

    print("*Vertices", numberNodes)
    print("*Edges")
    for i in range(0, numberNodes):
        for j in range(i+1, numberNodes):
            if random.random() < probability:
                print(i+1, j+1)
                graph.add_edge(i, j)

if __name__ == "__main__":
    numberNodes = 500
    averegeDegree = float(sys.argv[1])
    probability = averegeDegree/(numberNodes - 1)# Ad = P * ( N - 1 ) => Ad/(N - 1) = P
    createGraph(numberNodes, probability)

