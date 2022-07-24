from readInput import ReadInput
from grafo import Grafo

class Grafo_dirigido(Grafo):
    def __init__(self, vertices, vertices_array, arestas) -> None:
        super().__init__(vertices,vertices_array,arestas)

    def vizinhos_plus(self, v):
        vizinhanca = []
        
        for i in range(len(self.arestas)):
            inicio = self.arestas[i].inicio
            fim = self.arestas[i].fim
            if (inicio == v):
                vizinhanca.append(fim)
        vizinhanca = list(set(vizinhanca))    
        return vizinhanca  

    def haAresta(self, u, v):
        for i in range(len(self.arestas)):
            inicio = self.arestas[i].inicio
            fim = self.arestas[i].fim
            if(inicio == u and fim == v):
                return True
        return False    
    

    def peso(self, u, v):
        for i in range(len(self.arestas)):
            inicio = self.arestas[i].inicio
            fim = self.arestas[i].fim
            if(inicio == u and fim == v):
                return self.arestas[i].peso

    def get_arestas_transpostas(self):
        aresta_transpostas = []
        for aresta in self.arestas:
            aresta_transpostas.append(Aresta(aresta.fim,aresta.inicio,aresta.peso))
        return aresta_transpostas


class Aresta:
    def __init__(self, inicio, fim, peso) -> None:
        self.inicio = inicio
        self.fim = fim
        self.peso = peso

    def __str__(self) -> str:
        return f"{self.inicio}-{self.fim}:{self.peso}"