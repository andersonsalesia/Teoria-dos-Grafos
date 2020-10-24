from struct import grafo, vertice
from utils.util import Busca

# Instanciação da classe Grafo
grafo = grafo.Grafo('G1')

# Criação de vértices 
v1 = vertice.Vertice('V1')
v2 = vertice.Vertice('V2')
v3 = vertice.Vertice('V3')
v4 = vertice.Vertice('V4')
v5 = vertice.Vertice('V5')
v6 = vertice.Vertice('V6')  


# Adiciona os vértices no grafo
grafo.adicionar_vertice(v1)
grafo.adicionar_vertice(v2)
grafo.adicionar_vertice(v3)
grafo.adicionar_vertice(v4)
grafo.adicionar_vertice(v5)
grafo.adicionar_vertice(v6)


# Adiciona as arestas aos vértices
v1.adicionar_aresta(v2)
v1.adicionar_aresta(v3)

v2.adicionar_aresta(v1)
v2.adicionar_aresta(v3)
v2.adicionar_aresta(v4)
v2.adicionar_aresta(v5)

v3.adicionar_aresta(v1)
v3.adicionar_aresta(v2)
v3.adicionar_aresta(v4)

v4.adicionar_aresta(v2)
v4.adicionar_aresta(v3)

v5.adicionar_aresta(v2)
v5.adicionar_aresta(v6)

v6.adicionar_aresta(v5)

print(f"{grafo.nome}: {grafo.numero_de_vertices()} vertice(s) :{grafo}")

for vertice in grafo.vertices:
  print(f"{vertice.nome}: {vertice.numero_de_arestas()} aresta(s): {vertice.arestas}")

# print("--- Iniciando busca em largura ---")
# Busca.largura(grafo.vertices[0])

# grafo.ehConexo()

