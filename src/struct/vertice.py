class Vertice:
  def __init__(self, nome, visitado = False, explorado = False):
    self.nome = nome
    self.arestas = []
    self.visitado = visitado
    self.explorado = explorado

  def numero_de_arestas(self):
    return len(self.arestas)

  def adicionar_aresta(self, vertice):
    self.arestas.append(vertice)

  def __repr__(self):
    return f"{self.nome}"
    # return f"{self.nome}: {self.numero_de_arestas()} aresta(s): {self.arestas}"
