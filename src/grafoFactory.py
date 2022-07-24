from grafo import Aresta, Grafo
from grafo_dirigido import Grafo_dirigido
from readInput import ReadInput


class GrafoFactory:
    def __init__(self) -> None:
        pass
    
    def create_dirigido(self,fileName):
        file = ReadInput(fileName)
        info = file.read()
        dados = self.__mapearDados(info)
        return Grafo_dirigido(dados[0],dados[1], dados[2])

    def create(self, fileName) -> Grafo:
        file = ReadInput(fileName)
        info = file.read()
        dados = self.__mapearDados(info)
        return Grafo(dados[0], dados[1],dados[2])
    
    def __mapearDados(self, info):
        quantidadeVertices = 0
        vertices = {}
        vertices_array = []
        arestas = []
        for i in range(len(info)):

            if(i == 0):
                
                quantidadeVertices = int(info[i].split(" ")[1])
            
            elif(i <= quantidadeVertices):
               
                infoVertice = info[i].split(" ", 1)
                vertices[infoVertice[0]] = infoVertice[1]
                vertices_array.append(int(infoVertice[0]))
            
            elif(i > quantidadeVertices + 1):
                
                infoArestas = info[i].split(" ")
                inicio = infoArestas[0]
                fim = infoArestas[1]
                peso = infoArestas[2]
                arestas.append( Aresta(inicio, fim, peso))

        return [vertices,vertices_array, arestas]
        
                
