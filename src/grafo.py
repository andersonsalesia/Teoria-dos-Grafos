class Grafo:
  def __init__(self, nome):
    self.nome = nome
    self.vertices = []
  def adicionar_vertice(self, vertice):
    self.vertices.append(vertice)
  def numero_de_vertices(self):
    return len(self.vertices)
  def __repr__(self):
    return f"{self.vertices}"
