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
  
  def ehRegular(self) -> bool:
    primeiro_vertice = self.vertices[0]
    tamanho_primeiro_vertice = primeiro_vertice.numero_de_arestas()
    for vertice in self.vertices:
      if vertice.numero_de_arestas() != tamanho_primeiro_vertice:
        return False
    return True
