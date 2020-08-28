from graphviz import Digraph
import time
import numpy as np


def fibonacci2(x, g, l):
    if x <= 1:
        if x == 1:
            return 1
        if x == 0:
            return 0
    else:
        if l[x-1] == 0: 
            y = fibonacci2(x-1, g, l)
            l[x-1] = y
        else:
            y = l[x-1]
            
        if l[x-2] == 0: 
            z = fibonacci2(x-2, g, l)
            l[x-2] = z
        else:
            z = l[x-2]
                        
        g.edge(str(x), str(x-1))
        g.edge(str(x), str(x-2))
        return (y + z)


start = time.time()

graph = Digraph('G', filename='hello.gv')

num = 14
Arregloenteros = np.zeros((100))

print("The fibonacci of", num, "is", fibonacci2(num, graph, Arregloenteros))
print(Arregloenteros)

graph.view()

print("El Algoritmo demoro", round(time.time() - start), " Segundos")
