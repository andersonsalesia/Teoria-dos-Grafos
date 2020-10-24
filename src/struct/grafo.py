from .vertice import Vertice
from utils.util import Busca 

class Grafo:
  def __init__(self, nome):
    self.nome = nome
    self.vertices = []

  def adicionar_vertice(self, vertice):
    self.vertices.append(vertice)

  def numero_de_vertices(self):
    return len(self.vertices)

  def getAdjacentes(self, vertice: Vertice) -> list:
    return vertice.arestas
  
  def ehRegular(self) -> bool:
    primeiro_vertice = self.vertices[0]
    tamanho_primeiro_vertice = primeiro_vertice.numero_de_arestas()
    for vertice in self.vertices:
      if vertice.numero_de_arestas() != tamanho_primeiro_vertice:
        return False
    return True

  def ehCompleto(self) -> bool:
    for vertice in self.vertices:
      if len(vertice.arestas) != (self.numero_de_vertices() - 1):
        return False
    return True
  
  def ehConexo(self) -> bool:
    """
      # Aplica a busca em largura 
      # Se existir algum vértice que não foi visitado 
      # depois da busca em largura
      # então o grafo é desconexo
    """
    Busca.largura(self.vertices[0])
    for vertice in self.vertices:
      if vertice.visitado == False:
        print(f"{vertice.nome}(visitado={vertice.visitado}) depois da largura")
        return False
    return True
    

  def __repr__(self):
    return f"{self.vertices}"