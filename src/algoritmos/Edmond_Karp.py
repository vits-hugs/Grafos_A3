import sys
sys.path.append('..')
from grafo_dirigido import Grafo_dirigido
from grafoFactory import GrafoFactory


def Edmond_Karp(grafo: Grafo_dirigido):
    qtdV = grafo.qtdVertices()
    C = [False]*qtdV
    A = [None]*qtdV    
    C[0] = True
    Q = []
    Q.append(grafo.vertices_array[0])
    while Q != []:
        u = Q.pop(0)
        for vertice in grafo.vizinhos_plus(u):
            if C[vertice-1] == False:
                print(vertice)






g_dirigido = GrafoFactory().create_dirigido("dirigido.net")


Edmond_Karp(g_dirigido)


