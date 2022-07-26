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
            
    return -1

def Edmonds_Karp(grafo:Grafo_dirigido):
    print(grafo.fluxo)
    p = 0
    while p != -1:
        p = busca_largura_ed_Karp(grafo)
        #cf(p) = min(cf(u,v):(u,v) e p)
        arestas = get_arestas(grafo,p)
        minimo = min_arestas(grafo,arestas)
        for aresta_index in arestas:
            aresta = grafo.arestas[aresta_index]
            if grafo.haAresta(aresta.inicio,aresta.fim):
                grafo.fluxo[aresta_index] + minimo
            else:
                grafo.fluxo[aresta_index] - minimo#bagulho da capacidade
                
        #    else:
        #        pass


def verify_aresta(grafo:Grafo_dirigido,u,v):
    ind =  grafo.get_index_aresta(u,v)
    if ind == -1:
        return 0
    return grafo.arestas[ind].peso - grafo.fluxo[ind]

def get_arestas(grafo:Grafo_dirigido,p):
    arestas = []
    for x in range(1,len(p)):
        ind = grafo.get_index_aresta(p[x-1],p[x])
        arestas.append(ind)    
    return arestas

def min_arestas(grafo: Grafo_dirigido, arestas_i):#pelo custo
    menor_a = grafo.arestas[arestas_i[0]]
    menor = grafo.arestas[arestas_i[0]].peso
    for i in arestas_i:
        aresta = grafo.arestas[i]
        if aresta.peso < menor:
            menor = aresta.peso
            menor_a = aresta 
    return menor
g_dirigido = GrafoFactory().create_dirigido("dirigido.net")



for x in g_dirigido.arestas:
    print(x)


Edmonds_Karp(g_dirigido)
