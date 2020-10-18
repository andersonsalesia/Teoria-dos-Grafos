from struct.vertice import Vertice

class Busca:
  def largura(vertice: Vertice):
    fila = []
    vertice.visitado = True
    fila.append(vertice)

    while len(fila) != 0:
      last = fila[0]
      del fila[0]
      for adj in last.arestas:
        if not adj.visitado:
          adj.visitado = True
          fila.append(adj)
          print(fila)
      print(fila)