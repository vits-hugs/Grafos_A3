from readInput import ReadInput


class Grafo:
    def __init__(self, vertices,vertice_array, arestas) -> None:
        self.vertices = vertices
        self.vertices_array = vertice_array
        self.arestas = arestas
    
    def qtdVertices(self):
        return len(self.vertices)
    
    def qtdArestas(self):
        return len(self.arestas)

    def grau(self, v):
        grau = 0
        
        for i in range(len(self.arestas)):
            if(self.arestas[i].inicio == v or self.arestas[i].fim == v):
                grau +=1
        return grau
    
    def rotulo(self, u):
        rotulo = self.vertices.get(u)
        if(rotulo == None):
            raise KeyError("vertice not found")
        else:
            return rotulo

    def vizinhos(self, v):
        vizinhanca = []
        
        for i in range(len(self.arestas)):
            inicio = self.arestas[i].inicio
            fim = self.arestas[i].fim

            if(inicio == v or fim == v):
                vizinho = None
                if( inicio != v):
                    vizinho = inicio
                else:
                    vizinho = fim
                
                vizinhanca.append(vizinho)
        vizinhanca = list(set(vizinhanca))    
        return vizinhanca

    
    def haAresta(self, u, v):
        for i in range(len(self.arestas)):
            inicio = self.arestas[i].inicio
            fim = self.arestas[i].fim

            if(inicio == u and fim == v or inicio == v and fim == u):
                return True
        return False    
    

    def peso(self, u, v):
        for i in range(len(self.arestas)):
            inicio = self.arestas[i].inicio
            fim = self.arestas[i].fim
            if(inicio == u and fim == v or inicio == v and fim == u):
                return self.arestas[i].peso


class Aresta:
    def __init__(self, inicio, fim, peso) -> None:
        self.inicio = int(inicio)
        self.fim = int(fim)
        self.peso = float(peso)

    def __str__(self) -> str:
        return f"{self.inicio}-{self.fim}:{self.peso}"

    