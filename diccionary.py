from algo1 import*
import linkedlist

def createDiccionary(m):
  dic = Array(m,linkedlist.LinkedList())
  return dic
      
"""Ejercicio 1"""
"""función de hash"""
def h(k,m):
  return (ord(k[0]) % m)

""" Ejercicio 2 """
"""insert(D,key, value)
Descripción: Inserta un key en una posición determinada por la función de hash (1)  en el diccionario (dictionary). Resolver colisiones por encadenamiento. En caso de keys duplicados se anexan a la lista.
Entrada: el diccionario sobre el cual se quiere realizar la inserción  y el valor del key a insertar 
Salida: Devuelve D"""

def insert(D,key,value):
  k = h(key,len(D))
  key_value = (key,value) 
  if D[k] == None:
    L = linkedlist.LinkedList()
    linkedlist.add(L,key_value)
    D[k] = L
  else:
    linkedlist.add(D[k],key_value)
  return D
  
"""search(D,key)
Descripción: Busca un key en el diccionario
Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y el valor del key a buscar.
Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra."""

def search(D,key):
  k = h(key,len(D))
  if D[k] == None:
    return None
  else:
    node = D[k].head
    while node != None:
      if node.value[0] == key:
        return node.value[1]
      node = node.nextNode
    return None

"""delete(D,key)
Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary) 
Poscondición: Se debe marcar como nulo  el key  a eliminar.  
Entrada: El diccionario sobre el se quiere realizar la eliminación  y el valor del key que se va a eliminar.
Salida: Devuelve D"""

def delete(D,key):
  k = h(key,len(D))
  if D[k] == None:
    return D
  elif D[k].head.value[0] == key:
    if D[k].head.nextNode == None:
      D[k] = None
    else:
      node = D[k].head.nextNode 
      D[k].head == None
      D[k].head = node
    return D
  else:
    node = D[k].head
    while node.nextNode != None:
      if node.nextNode.value[0] == key:
        node.nextNode = node.nextNode.nextNode
        return D
      node = node.nextNode
    return D

" MUESTRA EN CONSOLA UN HASH TABLE COMPLETO"
def printHashtable(Dic):
  for i in range(0,len(Dic)):
    if Dic[i] == None:
      print("[",Dic[i],"]")
    else:
      currentNode = Dic[i].head
      while currentNode!= None:
        print("[",currentNode.value[1],"] ",end = " ")
        currentNode = currentNode.nextNode
      print(" ")