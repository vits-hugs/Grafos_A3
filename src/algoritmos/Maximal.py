import sys
import itertools
sys.path.append('..')
from grafo import Grafo
from grafoFactory import GrafoFactory

def num_filter(tupla,i):
    if i in tupla:
        return True
    return False

def generate_subconjuntos(lista):
    stuff = lista
    a = []
    for L in range(0, len(stuff)+1):
        for subset in itertools.combinations(stuff, L):
            a.insert(0,subset)
    return a

def Conjuntos_independentes_maximais(grafo:Grafo):
    S = generate_subconjuntos(grafo.vertices_array)
    print(S)
    R = []
    for subconjunto in S:
        c= True
        for v in subconjunto:
            for u in subconjunto:
                if  grafo.haAresta(u,v):
                    c = False
                    break
        
        if c:
            #remover todos os subconjuntos
            
            for x in subconjunto:
                S = filter(lambda f:num_filter(f,x),S)
            R.append(subconjunto)

    return R


grafo = GrafoFactory().create("flnpequena.txt")
print(Conjuntos_independentes_maximais(grafo))
