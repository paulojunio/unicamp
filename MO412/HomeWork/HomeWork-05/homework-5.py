"""
Forth HomeWork
Student: Paulo Junio Reis Rodrigues
"""
import networkx as nwx
import matplotlib.pyplot as plt
import numpy as np

def CreateGraph(n):
    graph = nwx.grid_2d_graph(n,n)
    print(nwx.info(graph))
    print(f'number of nodes {n*n}, number of links {2*n*n - n*2}, degree aaa {(4*n*n - n*4)/ (n*n)}')
    #print(graph.degree([0,1]))
    #print(nwx.average_shortest_path_length(graph))
    #print(nwx.degree(graph)[0])
    # nwx.draw(graph)
    # plt.show()
    sum = 0
    contador = 0
    for i in range(0,n):
        for j in range(0, n):
            pars = nwx.shortest_path_length(graph, source=(i, j))
            array = np.zeros((n*n), dtype=int)
            for r in range(0,n):
                for s in range(0, n):
                    ir = i - r
                    js = j - s
                    if (ir <= 0):
                        ir = ir * -1
                    if (js <= 0):
                        js = js * -1
                    #print(sum)
                    array[(n * r)+s] = ir + js
                    sum += (ir + js)
                    contador += 1
            #print(array)
            #print(array.sum())

    #print(contador)

    #print((2 * (n * n - 1)) / (3 * n))
    #print(sum/contador)
    return (sum/contador)

#Plot degree distribution with normal scale
def PlotNormalScale(arrayUm, arrayDois):
    plt.plot(arrayUm[0:], arrayDois[0:], 'ro-')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    arrayUm = np.zeros((19), dtype=float)
    arrayDois = np.zeros((19), dtype=float)
    for i in range (2,6):
        arrayUm[i-2] = i
        arrayDois[i-2] = CreateGraph(i)

    print(arrayUm)
    print(arrayDois)
    PlotNormalScale(arrayUm,arrayDois)


