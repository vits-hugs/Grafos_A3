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
            if C[vertice-1] == False and verify_aresta(grafo,u,vertice):
                C[vertice-1] = True
                A[vertice-1] = u

                if vertice == grafo.vertices_array[-1]:
                    p = [grafo.vertices_array[-1]]
                    w = grafo.vertices_array[-1]
                    while w!=grafo.vertices_array[0]:
                        w = A[w-1]
                        p.append(w)
                    return p 
                Q.append(vertice)
            

def Edmonds_Karp(grafo:Grafo_dirigido):
    p = busca_largura_ed_Karp(grafo)
    print(grafo.fluxo)
    while p != -1:
        pass
        #cf(p) = min(cf(u,v):(u,v) e p)
        for aresta in p:
            if grafo.haAresta(aresta.inicio,aresta.fim):
                pass
            else:
                pass


def verify_aresta(grafo:Grafo_dirigido,u,v):
    ind =  grafo.get_index_aresta(u,v)
    if ind == -1:
        return 0
    return grafo.arestas[ind].peso - grafo.fluxo[ind]

g_dirigido = GrafoFactory().create_dirigido("dirigido.net")


busca_largura_ed_Karp(g_dirigido)

for x in g_dirigido.arestas:
    print(x)


