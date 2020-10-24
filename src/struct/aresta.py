from .vertice import Vertice

class Aresta:
  def __init__(self, origem: Vertice, destino: Vertice, peso: int):
    self.origem = origem
    self.destino = destino
    self.peso = peso
    
  def __repr__(self):
    return f"{self.destino}"