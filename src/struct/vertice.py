class Vertice:
  def __init__(self, nome, visitado = False, explorado = False, valor = 0):
    self.nome = nome
    self.arestas = []
    self.adj = []
    self.visitado = visitado
    self.explorado = explorado
    self.valor = valor

  def numero_de_arestas(self):
    return len(self.arestas)

  # def adicionar_aresta(self, vertice):
  #   self.arestas.append(vertice)

  def adicionar_vertice(self, vertice):
    self.adj.append(vertice)

  def adicionar_aresta(self, aresta):
    self.arestas.append(aresta)

  def __repr__(self):
    return f"{self.nome}"
    # return f"{self.nome}: {self.numero_de_arestas()} aresta(s): {self.arestas}"
