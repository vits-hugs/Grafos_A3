import sys
sys.path.append('..')
from grafo_dirigido import Grafo_dirigido
from grafoFactory import GrafoFactory



def busca_largura_ed_Karp(grafo: Grafo_dirigido):
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

def Edmonds_Karp(grafo:Grafo_dirigido):
    fluxo = [0]*grafo.qtdArestas()
    p = busca_largura_ed_Karp(grafo)
    while p != -1:
        pass
        #cf(p) = min(cf(u,v):(u,v) e p)
        for aresta in p:
            if grafo.haAresta(aresta.inicio,aresta.fim):
                pass
            else:
                pass
            


g_dirigido = GrafoFactory().create_dirigido("dirigido.net")


busca_largura_ed_Karp(g_dirigido)


