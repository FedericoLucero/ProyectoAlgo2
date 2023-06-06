import linkedlist
from algo1 import*

"""tercer tipo de grafo con diccionarios"""

def createGraph(ListV,ListA):
  G = {}
  for vertice in ListV: # Recorre cada vertice
    G[vertice] = {} # Agregar vertices al grafo
      
  for arista in ListA: # recorre cada arista
    origen, destino, distancia = arista
    G[origen][destino] = distancia # Agrega aristas al grafo 
  return G

def printGraph(diccionario):
  print("{")
  for clave, valor in diccionario.items():
    print(f"    '{clave}': {valor},")
  print("}")

"""primer tipo de grafo con nodos == numero"""

"""
def createGraph(List,List) 
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos representa una conexión entre dos vértices.
Salida: retorna el nuevo grafo
"""
 
"""
#O(A+V)
def createGraph(ListV, ListA):
  n = len(ListV)
  G = Array(n,linkedlist.LinkedList())
  for i in range(0,n):
    G[i] = linkedlist.LinkedList()
    linkedlist.add(G[i],ListV[i])
  for i in ListA:
    linkedlist.insert(G[i[0]], i[1],1)
    linkedlist.insert(G[i[1]], i[0],1)
  return G 
"""

"""
#O(V+A)
def printGraph(G):
  for i in range(0,len(G)):
    if G[i] == None:
      print("[",G[i],"]")
    else:
      currentNode = G[i].head
      while currentNode!= None:
        print("[",currentNode.value,"] ",end = " ")
        currentNode = currentNode.nextNode
      print(" ")
"""

"""sugundo tipo de grafo con nodos == vertex , elemento == nodos.value"""

"""
class Vertex: #para que sea mas facil inicializar (value,color,etc)
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
    nodo.value = ListV[i]
    G[i] = linkedlist.LinkedList()
    linkedlist.add(G[i],(nodo,0)) # ponderado

  for i in ListA: # insert(L,element,posicion)
    linkedlist.insert(G[i[0]], G[i[1]].head.value,1) # dirigido
    #linkedlist.insert(G[i[1]], G[i[0]].head.value,1)

  return G

def printGraph(G):
  if G == None:
    return
  for i in range(0,len(G)):
    if G[i] == None:
      print("[",G[i],"]")
    else:
      currentNode = G[i].head
      while currentNode!= None:
        print("[",currentNode.value.value,"] ",end = " ")
        currentNode = currentNode.nextNode
      print(" ")
"""
