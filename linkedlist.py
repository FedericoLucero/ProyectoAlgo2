
############
class LinkedList:
  head=None
  
class Node:
  key=None
  value=None
  nextNode=None
############
  
############ add(L,element)
def add(L,element):
  nodox=Node()
  nodox.value=element
  nodox.nextNode=L.head
  L.head=nodox
############

############ search(L,element)
def search(L,element):
  cont=0
  pos=None
  currentNode=L.head
  while currentNode != None:
    if currentNode.value==element:
      pos=cont
      
    if pos == cont:
      currentNode=None
    else:
      currentNode=currentNode.nextNode
      cont=cont+1
  return pos
############
  
############ insert(L,element,position)
def insert(L,element,position):
  len=length(L)

  if len >= position:
    if len == 0:
      nodox=Node()
      nodox.value=element
      L.head=nodox
  
    else: 
      nodox=Node()
      nodox.value=element
      cont=0
      x=0
      currentNode=L.head
      while currentNode != None and x==0 :
        if cont == position-1:
          if currentNode.nextNode != None:
            nodox.nextNode= currentNode.nextNode
          currentNode.nextNode=nodox   
          x=1
        currentNode=currentNode.nextNode
        cont=cont+1
  else:
    position=None
  return position
############

############ delete(L,element)
def delete(L,element):
  currentNode=L.head
  pos=search(L,element)
  if pos != None:
    if pos != 0:
      currentNode=L.head
      cont=0
      while currentNode!= None and cont < pos:
        if cont == pos-1:
          currentNode.nextNode=currentNode.nextNode.nextNode
        currentNode=currentNode.nextNode
        cont=cont+1
    else:
      L.head=currentNode.nextNode
  return pos
############

############ length(L)
def length(L):
  currentNode=L.head
  len=0
  while currentNode!= None:
    len=len+1
    currentNode=currentNode.nextNode
  return len
############

############ access(L,position)
def access(L,position):
  element=None
  cont=0
  currentNode=L.head
  while currentNode!= None and cont<=position:
    if cont==position:
      element=currentNode.value
    cont=cont+1
    currentNode=currentNode.nextNode
  return element
############

############ update(L,element,position)
def update(L,element,position):
  
  len=length(L)
  
  if len >= position:
    cont=0
    currentNode=L.head
    while currentNode!= None and cont<=position:
      if cont==position:
        if currentNode.value==None:
          position=None
        else:
          currentNode.value=element
          position=cont
      cont=cont+1
      currentNode=currentNode.nextNode
  else:
    position=None

  return position
############
  
"mylinkedlist"
  
###########
def print_list(L):
  if L == None:
    print("[LISTA VACIA]")
  else:
    if L.head == None:
      print("[LISTA VACIA]")
    elif L.head.nextNode == None:
      print("[", L.head.value, "]" )
    else:
      currentNode=L.head
      while currentNode!= None:
        if currentNode==L.head:
          print("[ ",end="")
          print(currentNode.value,", ", end="")
          currentNode=currentNode.nextNode
        else:
          if currentNode.nextNode!= None:
            print(currentNode.value,", ", end="")
            currentNode=currentNode.nextNode
          else:
            print(currentNode.value,"]", end="")
            currentNode=currentNode.nextNode
      print("")
############
  
############
def swapNodes(L, node1, node2):
  head_ref = L.head
  head = head_ref
  if (node1 == node2):
    return None
  a = None
  b = None
  while (head_ref.nextNode != None):
    if (head_ref.nextNode == node1):
      a = head_ref
    elif (head_ref.nextNode == node2):
      b = head_ref
    head_ref = (head_ref.nextNode)

  if (a != None and b != None):
    temp = a.nextNode
    a.nextNode = b.nextNode
    b.nextNode = temp
    temp = a.nextNode.nextNode
    a.nextNode.nextNode = b.nextNode.nextNode
    b.nextNode.nextNode = temp
    
  elif (a == None and b != None): # a == cabeza
    temp1 = L.head
    temp2 = b.nextNode

    L.head = L.head.nextNode
    temp1.nextNode = None
    b.nextNode = temp1
    temp1.nextNode = temp2.nextNode
    temp2.nextNode = L.head
    L.head = temp2
############

############
def accessNode(L, position):
  currentNode = L.head
  if position >= 0:
    for i in range(0, position):
      if currentNode == None:
        return None
      currentNode = currentNode.nextNode
    return currentNode
############

############
def insertNode (L, Node, position):
  Node.nextNode = None
  if position == 0:
    Node.nextNode = L.head
    L.head = Node
    return position

  if position > 0:
    currentNode = L.head
    pos = 0
    while (currentNode != None):
      if pos + 1 != position:
        currentNode = currentNode.nextNode
        pos = pos + 1
      else:
        Node.nextNode = currentNode.nextNode
        currentNode.nextNode = Node
        pos = pos + 1
        return position
    return None
############
    
############
def dequeueNode(L):
  if L.head == None:
    return None
  currentNode = L.head
  while currentNode.nextNode != None:
    aux = currentNode
    currentNode = currentNode.nextNode
  aux.nextNode = None
  return currentNode
############

############
def enqueueNode(L, Node):
  if L.head != None:
    if Node != None:
      Node.nextNode = None
      currentNode = L.head
      while currentNode.nextNode != None:
        currentNode = currentNode.nextNode
      currentNode.nextNode = Node
  else:
    L.head = Node
    Node.nextNode = None
  return L

############

############
def addNode(L, Node):
  if L.head == None:
    L.head = Node
    Node.nextNode = None
  else:
    Node.nextNode = L.head
    L.head = Node
  return L
############

def push(S, element):
  add(S, element)
  return element

def pop(S):
  if S.head != None:
    currentNode = S.head.nextNode
    element = S.head.value
    S.head.nextNode = None
    S.head = currentNode
    return element
  else:
    return None
  
  #aaaaaaaaaa