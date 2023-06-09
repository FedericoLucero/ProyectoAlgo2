from uber import*
import pickle
import re

"""
Clases
"""

class fix_element():
    nombre = None
    direccion = None

class movil_element():
    nombre = None
    direccion = None
    monto = None

""" 
def read_lines(local_path):
Descripcion: lee la linea 1 y 2 del local_path devolviendo dos strings
"""
def read_lines(local_path):
    archive = open(local_path) # Abre el archivo en modo lectura ("r")
    try:
        line1 = archive.readline()
        line2 = archive.readline()
    finally:
        archive.close()
    return line1,line2

""" 
def Create_V_A(line1,line2):
Descripcion: lee los strings linea 1 y 2 convirtiendolos en dos listas
Salidas: 
{ Vertices = ["ex","ey","ez",...],
  Aristas = [("ex","ey",int),...] }
"""

def Create_V_A(line1,line2):
    Vertices = [v for v in re.findall(r'(e\d+)', line1)] # Extrae "e" seguido de los dígitos como un string

    valores = re.findall(r'(e\d+),(e\d+),(\d+)', line2) # Extraer "e" seguido de los dígitos como una cadena de texto en la 3-tupla
    Aristas = [(v[0], v[1], int(v[2])) for v in valores] # Convertir los valores en una lista de 3-tuplas
    return Vertices, Aristas

""" 
defcreate_address(direccion):
Descripcion: lee el strings ingresado como direccion y devuelve una lista de un par de tuplas
Salidas: 
{ direccion = [("ex",int),("ey",int)] }
"""

def create_address(direccion):
    valores = re.findall(r'(e\d+),(\d+),(e\d+),(\d+)', direccion)  # Extrae "e" seguido de los dígitos como una cadena de texto 
    Direccion = [((valores[0][0]), int(valores[0][1])), ((valores[0][2]), int(valores[0][3]))] # Convertir los valores extraídos en una lista de dos tuplas, con el primer elemento como cadena de texto y el segundo como entero
    return Direccion

""" 
def check_element(Ubicaciones,nombre):
Descripcion: comprueba una serie de condiciones para insertar el valor en el hash table
Salidas: 
{ True = cumple todas las condicones ,
  False = NO cumple al menos una condicon }
"""

def check_element(Ubicaciones,nombre):
    if diccionary.search(Ubicaciones,nombre) == None: # verifica si ya existe el nombre, if == None, no existe
        #if verificar que la direccion no este ocupada
            #if verificar que la direccion no tenga errores de dsitancia
                #if verifica que la direccion sea existente
                    return True
    return False

""" 
def open_file_load(archivo,modo):
Descripcion: Carga el contenido del archivo en una variable
Salidas: { variable }
"""

def open_file_load(archivo,modo):
    with open(archivo, modo) as f: # Abre el archivo en modo lectura 
        variable = pickle.load(f) # Cargar el contenido del archivo en la variable 
        return variable
    
""" 
def open_file_dump(archivo,modo,variable):
Descripcion: guarda el contenido de la variable en el archivo
"""

def open_file_dump(archivo,modo,variable):
    with open(archivo, modo) as f: # Abrir el archivo en modo de escritura
        pickle.dump(variable, f) # Guardar el contenido en el archivo
        
        
def create_map_dictionary(Vertices,Aristas):
    uberMap = dict() #defino el objeto como un dict vacio para poder acceder luego a todos los vertices 
    for vertice in Vertices: # Recorre cada vertice  
        grafo[vertice] = {} # Agregar vertices al grafo 
        uberMap[vertice] = dict() #Defino cada vertice como un diccionario vacio para que  luego pueda acceder a "[origen][destino]" 
        
    for arista in Aristas: # recorre cada arista  
        origen, destino, distancia = arista
        grafo[origen][destino] = distancia # Agrega aristas al grafo  
        newAddress = domain.Distance() #Genera objeto de tipo Distance 
        newAddress.Distance=distancia #asigna el valor de distancia de la arista al dicho objeto  
        uberMap[origen][destino] = newAddress #genera  en la estuctura "ubermap" la arista correspondiente con las aristas "directas" 
        
    for origin in uberMap: #recorre todos los vertices originales
        for newOrigin in uberMap: #por cada vez que se recorren arriba, los vuelve a recorrer para conectarlos y con ellos recorrer las subconecciones
            if newOrigin == origin:
                continue
            try:
                baseCon = uberMap[newOrigin][origin] #Intenta acceder a la una conexion posible entre 2 vertices A y B, de no existir, dispara except 
                nextNode = baseCon.NearNodeInWay #Guarda el nodo mas cercao de la conexion si es que existiese
                if nextNode == None:
                    nextNode = origin #de no existir, quiere decir que es un arista directa entre 2 vertices, por lo que el "proximo nodo" va a ser el nodo B
                #Si llega a este punto del codigo, quiere decir que existe una conexion entre A y B
                for newDest in uberMap[origin]: # por lo que recorro el dict de B para acceder a sus aristas y poder crear las mismas en el diccionario del vertice B
                    newDistance = baseCon.Distance + uberMap[origin][newDest].Distance #la distancia base que va a tener la nueva conexion va a ser, la distancia entre A y B y la distancia entre B y cada nodo X en su DICT
                    try:
                        existingCon = uberMap[newOrigin][newDest] #Intento acceder a una conexion previa entre el nodo A y X, de no existir, voy a exec
                        if existingCon.Distance > newDistance: #De existir una conexion, analizo si la nueva conexion que quiero crear tiene menos costo que la que ya existia
                            uberMap[newOrigin][newDest].NearNodeInWay = nextNode #si tiene menos costo, accedo a esa dicha direccion
                            uberMap[newOrigin][newDest].Distance = newDistance
                    except:
                        linkedAddress = domain.Distance() #Creo una nueva conexion con los datos encontrados anteriormente
                        linkedAddress.Distance = newDistance 
                        linkedAddress.NearNodeInWay = nextNode
                        uberMap[newOrigin][newDest] = linkedAddress  #Ahora existe una nueva conexion (directa o no) entre A y X con distancia "newDistance" y "nextNode" de proximo nodo
            except:
                continue
    return uberMap

def print_all_nodes(uberMap):
    for o in uberMap:
        for d in  uberMap[o]:
            print("origen",o,"destino",d,"costo",uberMap[o][d].Distance, "nextNode",uberMap[o][d].NearNodeInWay)