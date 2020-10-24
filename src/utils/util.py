from struct.vertice import Vertice

class Busca:
  def largura(vertice: Vertice):
    fila = []
    vertice.visitado = True
    fila.append(vertice)

    while len(fila) != 0:
      last = fila[0]
      del fila[0]
      for adj in last.adj:
        if not adj.visitado:
          adj.visitado = True
          fila.append(adj)
          print(fila)
      print(fila)
      
  # def dijstra(grafo):
  #   # Seja S um conjunto de vértices inicialmente com seu vértice origem;
  #   s: list = []
    
  #   # Pegar o primeiro vértice e o define como origem vértice origem
  #   t = grafo.vertices[0]

  #   # Coloca o o valor da distancia do vértice raiz como 0
  #   t.valor = 0
  #   # vamos assumir um conjunto S que contém inicialmente somente a raiz; 
  #   s.append(t)

  #   for vertice in s:
  #     for adj in vertice.arestas:
  #       if adj.dist >
