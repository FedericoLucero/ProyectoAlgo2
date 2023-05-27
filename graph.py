class Nodo:
  def __init__(self, identificador):
    self.id = identificador
    self.aristas_salientes = []

class Arista:
  def __init__(self, destino, distancia):
    self.destino = destino
    self.distancia = distancia

def createGraph(vertices, aristas):
  grafo = []
  
  # Crear nodos
  for v in vertices:
    nodo = Nodo(v)
    grafo.append(nodo)
  
  # Agregar aristas salientes
  for origen, destino, distancia in aristas:
    nodo_origen = grafo[origen]
    arista = Arista(destino, distancia)
    nodo_origen.aristas_salientes.append(arista)
  
  return grafo

# Ejemplo de uso
#vertices = [0, 1, 2, 3, 4]
#aristas = [(0, 1, 5), (0, 4, 2), (1, 2, 3), (1, 3, 4), (1, 4, 1), (2, 3, 2), (3, 4, 3)]
#grafo = createGraph(vertices, aristas)

# Imprimir listas de adyacencia con distancias
#for nodo in grafo:
  #aristas_salientes = [(a.destino, a.distancia) for a in nodo.aristas_salientes]
  #print(f"Nodo {nodo.id}: {aristas_salientes}")


"""
import linkedlist
from algo1 import*
import re
"crea un grafo dirigido usando vertex"

class Vertex:
  value = None
  color = None
  d = None
  pi = None
  f = None

def createGraph(ListV, ListA):
  n = len(ListV)
  G = Array(n,linkedlist.LinkedList())
  for i in range(0,n):
    nodo = Vertex()
    # Extraer solo el entero después de la letra "e"
    entero = int(re.findall(r'\d+', ListV[i])[0])
    nodo.value = entero
    G[i] = linkedlist.LinkedList()
    linkedlist.add(G[i],nodo)
    linkedlist.print_list(G[i])

  for i in ListA:
    entero1 = int(re.findall(r'\d+', i[0])[0])
    entero2 = int(re.findall(r'\d+', i[1])[0])
    linkedlist.insert(G[entero1], G[entero2].head.value,1)
    #linkedlist.insert(GV[i[1]], GV[i[0]].head.value,1)
  return G
"""