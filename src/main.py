from struct import grafo, vertice, aresta
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

# V1
v1_a1 = aresta.Aresta(v1,v2, 5)
v1_a2 = aresta.Aresta(v1,v3, 10)

# Arestas
v1.adicionar_aresta(v1_a1)
v1.adicionar_aresta(v1_a2)

# Vertice
v1.adicionar_vertice(v2)
v1.adicionar_vertice(v3)

# V2
v2_a1 = aresta.Aresta(v2,v1, 5)
v2_a2 = aresta.Aresta(v2,v3, 10)
v2_a3 = aresta.Aresta(v2,v4, 10)
v2_a4 = aresta.Aresta(v2,v5, 10)

v2.adicionar_aresta(v2_a1)
v2.adicionar_aresta(v2_a2)
v2.adicionar_aresta(v2_a3)
v2.adicionar_aresta(v2_a4)

v2.adicionar_vertice(v1)
v2.adicionar_vertice(v3)
v2.adicionar_vertice(v4)
v2.adicionar_vertice(v5)

# V3
v3_a1 = aresta.Aresta(v3,v1, 5)
v3_a2 = aresta.Aresta(v3,v2, 10)
v3_a3 = aresta.Aresta(v3,v4, 10)

v3.adicionar_aresta(v3_a1)
v3.adicionar_aresta(v3_a2)
v3.adicionar_aresta(v3_a3)

v3.adicionar_vertice(v1)
v3.adicionar_vertice(v2)
v3.adicionar_vertice(v4)

# V4
v4_a1 = aresta.Aresta(v4,v2, 5)
v4_a2 = aresta.Aresta(v4,v3, 10)

v4.adicionar_aresta(v4_a1)
v4.adicionar_aresta(v4_a2)

v4.adicionar_vertice(v2)
v3.adicionar_vertice(v3)

# V5
v5_a1 = aresta.Aresta(v5,v2, 5)
v5_a2 = aresta.Aresta(v5,v6, 5)

v5.adicionar_aresta(v5_a1)
v5.adicionar_aresta(v5_a2)

v3.adicionar_vertice(v2)
v3.adicionar_vertice(v6)

# V6
v6_a1 = aresta.Aresta(v6, v5, 1)

v6.adicionar_aresta(v6_a1)

v3.adicionar_vertice(v5)

print(f"{grafo.nome}: {grafo.numero_de_vertices()} vertice(s) :{grafo}")

for vertice in grafo.vertices:
  print(f"{vertice.nome}: {vertice.numero_de_arestas()} aresta(s): {vertice.arestas}")

# print("--- Iniciando busca em largura ---")
# Busca.largura(grafo.vertices[0])

# print(grafo.ehConexo())
# print(grafo.ehRegular())
# print(grafo.getAdjacentes(grafo.vertices[0]))
# print(grafo.ehCompleto())
